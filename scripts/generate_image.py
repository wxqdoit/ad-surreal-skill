#!/usr/bin/env python3
"""
generate_image.py - Universal direct image generation utility for ad-surreal-skill.
Connects to the configured API endpoint to directly generate and save images.
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

def generate_image(prompt, out_path, model="grok-imagine-image-2.0", size="1024x1024"):
    base_url, api_key = get_auth_config()
    endpoint = f"{base_url}/images/generations"

    payload = {
        "model": model,
        "prompt": prompt,
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
                    # Download image from URL
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
    parser.add_argument("prompt", help="Visual prompt description")
    parser.add_argument("--out", "-o", required=True, help="Output image file path")
    parser.add_argument("--model", default="grok-imagine-image-2.0", help="Model name")
    parser.add_argument("--size", default="1024x1024", help="Image dimensions")

    args = parser.parse_args()

    success, path, error = generate_image(args.prompt, args.out, model=args.model, size=args.size)
    if success:
        print(json.dumps({"success": True, "path": path}, ensure_ascii=False))
    else:
        print(json.dumps({"success": False, "error": error}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
