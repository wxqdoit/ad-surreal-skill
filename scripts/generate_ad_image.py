#!/usr/bin/env python3
"""
generate_ad_image.py - Direct image generation and asset management for ad-surreal-skill.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
IMAGEGEN_SCRIPT = Path.home() / ".codex" / "skills" / ".system" / "imagegen" / "scripts" / "image_gen.py"

INDUSTRY_PRESETS = {
    "tech": {
        "name": "3C Tech & Computing",
        "materials": "matte space titanium, anodized dark gray aluminum, sapphire glass glints, subtle fiber-optic light glow",
        "lighting": "Profoto softbox key light with dual-tone crisp cyan and amber edge rim lighting, soft diffuse fill",
        "camera": "shot on Hasselblad H6D-100c, 85mm f/8 commercial lens, Octane 3D render fidelity, 8k resolution"
    },
    "luxury": {
        "name": "Luxury, Fragrance & Skincare",
        "materials": "heavy crystalline glass, golden amber serum droplets, raw travertine marble plinth, delicate botanical petals",
        "lighting": "sunlight through gentle water caustics, soft morning Tyndall rays, high-key diffuse lighting, subsurface scattering",
        "camera": "shot on Phase One XF IQ4 150MP, 100mm macro lens at f/5.6, dreamy soft focus"
    },
    "athletic": {
        "name": "Athletic & Performance Gear",
        "materials": "visible woven carbon fiber plate, micro-cellular supercritical foam, ballistic ripstop fabric, volcanic basalt rock",
        "lighting": "intense directional rim lighting, golden hour dust backlighting, stormy cinematic lightning glints",
        "camera": "ultra high-speed commercial action photography, 1/8000s shutter speed freeze, 70mm lens at f/4"
    },
    "auto": {
        "name": "Automotive & Mobility",
        "materials": "multi-coat liquid metallic lacquer, forged carbon aero splitters, razor-thin blade LED headlights",
        "lighting": "long-exposure twilight neon light trails, reflective wet asphalt surface reflections",
        "camera": "commercial cinematic automotive photography, low-angle heroic perspective, 35mm anamorphic lens"
    },
    "fmcg": {
        "name": "Food & Beverage",
        "materials": "frost and crystalline condensation droplets, pristine ice cubes, bursting fresh fruit slices, effervescent bubbles",
        "lighting": "backlit transparent liquid refraction, dazzling prism glints, bright crisp summer daylight",
        "camera": "high-speed fluid sculpture photography, macro liquid lens, 8k studio product photography"
    },
    "home": {
        "name": "Smart Home & Lifestyle",
        "materials": "natural light oak, porous travertine stone, bouclé fabric, brushed brass accents",
        "lighting": "soft diffuse window daylight casting architectural shadows, warm interior ambient glow",
        "camera": "modernist architectural interior photography, medium format, clean airy composition"
    }
}

METAPHOR_TEMPLATES = {
    "scale": {
        "title": "尺度奇观 / 宏观地标 (Scale Distortion)",
        "slogan": "方寸之间，容纳旷世之境",
        "action": "monumental architectural scale standing proudly like a modern monolithic sculpture in a vast expansive serene landscape, contrasted with tiny scale human silhouette",
        "copy_space": "clean generous negative space across the upper third for commercial typography"
    },
    "material": {
        "title": "物性反转与材质炼金 (Material Alchemy)",
        "slogan": "凝固澎湃，化刚为柔",
        "action": "materials seamlessly transforming into dynamic liquid silk and crystalline frozen splash sculptures, floating in zero-gravity over a minimalist pedestal",
        "copy_space": "spacious clean negative space on the left side reserved for brand typography"
    },
    "zerog": {
        "title": "失重瞬态与动力学定格 (Zero-G Kinetic Freeze)",
        "slogan": "静止的瞬间，万钧的爆发",
        "action": "suspended in bullet-time zero-gravity, exploding with dynamic kinetic particles and frozen fluid crowns, meticulous internal engineering floating in harmonious balance",
        "copy_space": "ample clean negative space for brand slogan at the top"
    },
    "synesthesia": {
        "title": "通感实体化与能量力场 (Synesthesia Force Field)",
        "slogan": "隔绝喧嚣，自成深蓝宇宙",
        "action": "surrounded by a visible translucent acoustic energy forcefield bubble, external chaotic noise waves dissolving into serene calm liquid ripples upon touching the barrier",
        "copy_space": "open minimalist negative space on top-left for copy"
    }
}

def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[-\s]+', '-', text).strip('-_') or "campaign"

def compile_commercial_prompt(product, usp, category="tech", metaphor_key="scale", aspect_ratio="3:4"):
    preset = INDUSTRY_PRESETS.get(category.lower(), INDUSTRY_PRESETS["tech"])
    metaphor = METAPHOR_TEMPLATES.get(metaphor_key.lower(), METAPHOR_TEMPLATES["scale"])

    # Midjourney / Commercial DALL-E Prompt
    prompt = (
        f"Award-winning commercial key visual, hero shot of {product} illustrating {usp}, "
        f"{metaphor['action']}, "
        f"{preset['materials']}, "
        f"{preset['lighting']}, "
        f"{metaphor['copy_space']}, "
        f"{preset['camera']} --ar {aspect_ratio} --v 6.1 --stylize 250 "
        f"--no text, letters, watermarks, logo, blurry textures, cheap plastic render, extra debris"
    )

    # Clean prompt for image generation APIs (without Midjourney parameter syntax)
    clean_prompt = (
        f"Award-winning commercial advertising key visual, hero product shot of {product}, "
        f"symbolizing {usp}. {metaphor['action']}. "
        f"Materials: {preset['materials']}. "
        f"Lighting: {preset['lighting']}. "
        f"{metaphor['copy_space']}. "
        f"{preset['camera']}."
    )

    return prompt, clean_prompt, metaphor, preset

def main():
    parser = argparse.ArgumentParser(description="Generate commercial key visual images and campaign prompts.")
    parser.add_argument("--product", required=True, help="Product name or description")
    parser.add_argument("--usp", required=True, help="Unique Selling Proposition / Core Benefit")
    parser.add_argument("--category", default="tech", choices=list(INDUSTRY_PRESETS.keys()), help="Industry category")
    parser.add_argument("--metaphor", default="scale", choices=list(METAPHOR_TEMPLATES.keys()), help="Surreal metaphor archetype")
    parser.add_argument("--ar", default="3:4", help="Aspect ratio (e.g. 3:4, 16:9, 1:1, 9:16)")
    parser.add_argument("--out-dir", default=None, help="Directory to save image and prompts")
    parser.add_argument("--generate", action="store_true", help="Directly invoke image generation")

    args = parser.parse_args()

    slug = slugify(args.product)
    out_dir = Path(args.out_dir) if args.out_dir else SKILL_ROOT / "output" / "campaigns" / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    mj_prompt, clean_prompt, metaphor, preset = compile_commercial_prompt(
        args.product, args.usp, args.category, args.metaphor, args.ar
    )

    prompt_file = out_dir / "prompt.md"
    image_file = out_dir / "kv.png"

    # Save prompt file
    prompt_content = f"""# Commercial Key Visual Brief: {args.product}
- **Category**: {preset['name']}
- **USP**: {args.usp}
- **Metaphor Archetype**: {metaphor['title']}
- **Slogan**: {metaphor['slogan']}
- **Aspect Ratio**: {args.ar}

## Midjourney v6.1 Prompt
```text
{mj_prompt}
```

## Clean Generation Prompt
```text
{clean_prompt}
```
"""
    prompt_file.write_text(prompt_content, encoding="utf-8")

    generated = False
    error_msg = None

    if args.generate:
        # Check if imagegen script exists
        if IMAGEGEN_SCRIPT.exists() and os.environ.get("OPENAI_API_KEY"):
            cmd = [
                "/Users/wxqdoit/.local/bin/uv", "run", "--with", "openai", "python3",
                str(IMAGEGEN_SCRIPT), "generate",
                "--prompt", clean_prompt,
                "--out", str(image_file),
                "--quality", "high"
            ]
            try:
                res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                if res.returncode == 0 and image_file.exists():
                    generated = True
                else:
                    error_msg = res.stderr or res.stdout
            except Exception as e:
                error_msg = str(e)
        else:
            error_msg = "Image generation requires a valid OPENAI_API_KEY or built-in image_gen tool."

    output_data = {
        "product": args.product,
        "usp": args.usp,
        "category": preset["name"],
        "metaphor": metaphor["title"],
        "slogan": metaphor["slogan"],
        "aspect_ratio": args.ar,
        "prompt_path": str(prompt_file),
        "image_path": str(image_file) if generated else None,
        "mj_prompt": mj_prompt,
        "clean_prompt": clean_prompt,
        "generated": generated,
        "error": error_msg
    }

    print(json.dumps(output_data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
