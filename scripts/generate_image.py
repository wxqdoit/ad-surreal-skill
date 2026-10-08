#!/usr/bin/env python3
"""
generate_image.py - Universal direct image generation utility for ad-surreal-skill.
Connects to the configured API endpoint to directly generate and save images.
Supports curated commercial style presets.
"""

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent

STYLE_PRESETS = {
    "haute-couture": {
        "name": "法式高定静奢风 (Haute Couture Quiet Luxury)",
        "prompt_wrapper": (
            "Award-winning haute couture quiet luxury commercial fashion campaign. "
            "Subject: {prompt}. "
            "Background: seamless warm oatmeal and ecru studio backdrop, vast generous negative space taking up 70% of the composition. "
            "Gentle directional softbox window light from top-left creating soft natural shadows. "
            "In the upper-left corner, subtle fine-serif minimalist typography reads 'LUMIÈRE ÉTÉ'. "
            "Hasselblad 8k fashion photography, timeless refined elegance, zero clutter."
        )
    },
    "minimal-void": {
        "name": "科技极简纯粹留白风 (Pure Negative-Space Minimalist)",
        "prompt_wrapper": (
            "Award-winning minimalist commercial advertising key visual poster. "
            "Subject: {prompt} positioned elegantly in the lower-right third of the frame. "
            "Background: seamless studio cyclorama in ultra-pale warm alabaster tone, vast expansive clean negative space occupying 75% of the frame with soft breathing room, "
            "delicate subtle floor contact shadow, Profoto studio softbox lighting, crisp clean edges, Hasselblad commercial still life photography, Apple advertising aesthetic, 8k resolution, perfectly clean void, zero clutter."
        )
    },
    "color-block": {
        "name": "先锋现代撞色风 (Swiss Modern Graphic Color-Blocking)",
        "prompt_wrapper": (
            "Award-winning minimalist graphic commercial advertising key visual. "
            "Dramatic bold color blocking contrast, background divided into two pristine solid minimalist blocks: vibrant electric cobalt blue and warm apricot peach. "
            "Vast expansive negative space occupying 70% of the canvas. "
            "Subject: {prompt} positioned with crisp clean shadow. "
            "Minimalist Swiss graphic design aesthetic, pure void, zero clutter, 8k commercial photography."
        )
    },
    "cinematic-noir": {
        "name": "电影级暗调戏剧光影风 (Cinematic Chiaroscuro & Film Noir)",
        "prompt_wrapper": (
            "Award-winning cinematic commercial campaign photography. "
            "Subject: {prompt}. "
            "Atmosphere: dramatic chiaroscuro Rembrandt lighting, rich deep velvety shadows, delicate golden amber edge rim light, subtle atmospheric haze, "
            "vast moody negative space in deep charcoal tones, 35mm anamorphic lens, high narrative drama, timeless elegance."
        )
    },
    "sunlit-caustics": {
        "name": "地中海日光焦散风 (Mediterranean Sunlit Caustics)",
        "prompt_wrapper": (
            "Luxury commercial campaign poster bathed in Mediterranean morning sun. "
            "Subject: {prompt}. "
            "Lighting: sunlit water caustics dancing gracefully on clean travertine limestone surfaces, warm golden hour glow, "
            "airy expansive negative space in soft warm cream tones, high-key diffuse daylight, natural organic elegance."
        )
    },
    "cyber-photon": {
        "name": "先锋赛博光子风 (Midnight Cyber & Luminous Photon)",
        "prompt_wrapper": (
            "Futuristic commercial advertising key visual. "
            "Subject: {prompt}. "
            "Background: deep midnight void, dual-tone precision rim lights in electric cyan and glowing violet, subtle fiber-optic photon flow, "
            "spacious clean dark negative space for high-tech branding, ultra-sharp reflections, 8k Octane render quality."
        )
    },
    "botanical-surreal": {
        "name": "空灵植物超现实风 (Ethereal Botanical Surrealism)",
        "prompt_wrapper": (
            "High-concept luxury commercial key visual. "
            "Subject: {prompt} seamlessly harmonizing with translucent crystalline botanical flora and floating morning dew drops. "
            "Background: ethereal soft pastel gradient mist, vast airy negative space, soft diffuse god rays, poetic dreamlike tranquility, 8k fine art photography."
        )
    }
}

def get_auth_config():
    """Retrieve base_url and api_key from config or environment."""
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = "https://api.308437.xyz/v1"

    config_path = Path.home() / ".codex" / "config.toml"
    if config_path.exists():
        try:
            content = config_path.read_text(encoding="utf-8")
            url_match = re.search(r'base_url\s*=\s*"([^"]+)"', content)
            if url_match:
                base_url = url_match.group(1).rstrip("/")
        except Exception:
            pass

    auth_path = Path.home() / ".codex" / "auth.json"
    if auth_path.exists():
        try:
            auth_data = json.loads(auth_path.read_text(encoding="utf-8"))
            if "OPENAI_API_KEY" in auth_data and auth_data["OPENAI_API_KEY"]:
                api_key = auth_data["OPENAI_API_KEY"]
        except Exception:
            pass

    return base_url, api_key

def generate_image(prompt, out_path, model="grok-imagine-image-2.0", size="1024x1024", style_key=None):
    base_url, api_key = get_auth_config()
    endpoint = f"{base_url}/images/generations"

    final_prompt = prompt
    if style_key and style_key.lower() in STYLE_PRESETS:
        wrapper = STYLE_PRESETS[style_key.lower()]["prompt_wrapper"]
        final_prompt = wrapper.format(prompt=prompt)

    payload = {
        "model": model,
        "prompt": final_prompt,
        "n": 1,
        "size": size
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    req = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "data" in data and len(data["data"]) > 0:
                item = data["data"][0]
                out_path = Path(out_path)
                out_path.parent.mkdir(parents=True, exist_ok=True)
                
                if "b64_json" in item:
                    img_bytes = base64.b64decode(item["b64_json"])
                    out_path.write_bytes(img_bytes)
                    return True, str(out_path.resolve()), None
                elif "url" in item:
                    img_req = urllib.request.Request(item["url"])
                    with urllib.request.urlopen(img_req, timeout=60) as img_resp:
                        out_path.write_bytes(img_resp.read())
                    return True, str(out_path.resolve()), None
                else:
                    return False, None, "No b64_json or url in response."
            else:
                return False, None, f"Unexpected response: {data}"
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8", errors="ignore")
        return False, None, f"HTTP Error {e.code}: {err_msg}"
    except Exception as e:
        return False, None, str(e)

def main():
    parser = argparse.ArgumentParser(description="Universal image generator.")
    parser.add_argument("prompt", help="Visual prompt description or subject")
    parser.add_argument("--out", "-o", required=True, help="Output image file path")
    parser.add_argument("--style", "-s", choices=list(STYLE_PRESETS.keys()), default=None, help="Curated style preset")
    parser.add_argument("--model", default="grok-imagine-image-2.0", help="Model name")
    parser.add_argument("--size", default="1024x1024", help="Image dimensions")

    args = parser.parse_args()

    success, path, error = generate_image(args.prompt, args.out, model=args.model, size=args.size, style_key=args.style)
    if success:
        print(json.dumps({"success": True, "path": path}, ensure_ascii=False))
    else:
        print(json.dumps({"success": False, "error": error}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
