#!/usr/bin/env python3
"""
generate_campaign.py - CLI tool to quickly generate structured surreal commercial campaign proposals.
"""

import argparse
import json
import sys

INDUSTRY_PRESETS = {
    "tech": {
        "name": "3C Tech & Computing",
        "materials": "matte titanium, anodized space gray aluminum, ultra-clear sapphire glass, subtle fiber-optic light glow",
        "lighting": "Profoto softbox key light with dual-tone crisp cyan and amber edge rim lighting",
        "camera": "shot on Hasselblad H6D-100c, 85mm f/8 commercial lens, Octane 3D render fidelity, 8k resolution"
    },
    "luxury": {
        "name": "Luxury, Fragrance & Skincare",
        "materials": "heavy crystalline glass, golden amber serum droplets, raw travertine marble plinth, delicate botanical petals",
        "lighting": "sunlight through gentle water caustics, soft morning Tyndall rays, high-key diffuse lighting",
        "camera": "shot on Phase One XF IQ4 150MP, 100mm macro lens at f/5.6, dreamy soft focus"
    },
    "athletic": {
        "name": "Athletic & Performance Gear",
        "materials": "visible woven carbon fiber, micro-cellular supercritical foam, ballistic ripstop fabric, volcanic rock shards",
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

def generate_campaign(product, usp, category="tech", aspect_ratio="3:4"):
    preset = INDUSTRY_PRESETS.get(category.lower(), INDUSTRY_PRESETS["tech"])
    
    # 3 Distinct concepts
    concepts = [
        {
            "type": "尺度奇观 / 宏观地标 (Scale Distortion & Monumental Wonder)",
            "title": f"The Monolith of {product}",
            "slogan_zh": "方寸之间，容纳旷世之境",
            "slogan_en": "Beyond Ordinary Horizons",
            "metaphor": f"将 {product} 放大为百米高的自然地标巨构，矗立于极简地貌之上，戏剧化外显其 '{usp}' 的统治级实力。",
            "staging": "广袤空灵的极简雪山峡谷或反光盐湖，微弱晨雾与微小飞鸟作为比例参照，营造史诗感。",
            "copy_space": "顶部 35% 预留纯净负空间供广告标题排版 (Clean negative space at upper third for brand typography)",
            "mj_prompt": (
                f"Award-winning commercial key visual, monumental architectural scale of {product}, "
                f"symbolizing {usp}, standing proudly in a vast minimalist landscape with morning mist, "
                f"contrasted with tiny scale elements, {preset['materials']}, {preset['lighting']}, "
                f"clean generous negative space at the top reserved for headline typography, "
                f"{preset['camera']} --ar {aspect_ratio} --v 6.1 --stylize 250 "
                f"--no text, letters, watermarks, logo, blurry textures, cheap plastic render"
            ),
            "flux_prompt": (
                f"Commercial advertising campaign photography of {product}. The product is heroically scaled "
                f"like a sculptural architectural monument in a serene expansive landscape representing {usp}. "
                f"Materials feature {preset['materials']}. Studio lighting: {preset['lighting']}. "
                f"Clear open negative space on top for editorial text. Masterpiece studio quality."
            )
        },
        {
            "type": "物性反转与材质炼金 (Material Alchemy & Phase Transition)",
            "title": f"Fluid State of {product}",
            "slogan_zh": "凝固澎湃，化刚为柔",
            "slogan_en": "Pure Alchemy of Sensation",
            "metaphor": f"将传统固态结构转译为如液态金属丝绸与晶体雕塑的共生体，直观具象化 '{usp}' 的丝滑与纯粹感。",
            "staging": "极简悬浮底座，空中翻卷的液态材质与接触点瞬间凝结为剔透钻石多面体，折射出丰富焦散光斑。",
            "copy_space": "画面左侧 40% 预留柔和渐变负空间 (Generous negative space on the left side for copy)",
            "mj_prompt": (
                f"High-concept luxury commercial key visual, hero shot of {product} demonstrating {usp}, "
                f"materials seamlessly transforming into dynamic liquid silk and crystalline frozen splash sculptures, "
                f"floating in zero-gravity over a minimalist pedestal, {preset['materials']}, "
                f"intricate refractive caustics, subsurface scattering, {preset['lighting']}, "
                f"spacious clean negative space on the left for luxury typography, "
                f"{preset['camera']} --ar {aspect_ratio} --v 6.1 --stylize 300 "
                f"--no text, watermark, deformed, messy clutter, cartoon, plastic"
            ),
            "flux_prompt": (
                f"Editorial commercial poster featuring {product}. The product features surreal material transitions, "
                f"with fluid liquid elements freezing into crystalline structures highlighting {usp}. "
                f"Refined textures of {preset['materials']}. Atmospheric studio lighting with {preset['lighting']}. "
                f"Generous negative space on one side for typography."
            )
        },
        {
            "type": "失重瞬态动力学与矛盾置景 (Zero-G Explosion & Impossible Staging)",
            "title": f"Kinetic Symphony of {product}",
            "slogan_zh": "静止的瞬间，万钧的爆发",
            "slogan_en": "Suspended in Perpetual Motion",
            "metaphor": f"在零重力场中将 {product} 的核心动能瞬间定格，高速能量粒子与精密结构悬浮共振，外化 '{usp}' 的爆发张力。",
            "staging": "极简清水混凝土画廊空间穿透着悬浮的气流粒子与悬空悬停的精密部件，秩序与能量交织。",
            "copy_space": "画面上方预留纯色区域供排版 (Open copy space on the upper portion)",
            "mj_prompt": (
                f"Cannes Lions commercial advertising key visual, {product} suspended in bullet-time zero-gravity, "
                f"exploding with dynamic kinetic particles and frozen fluid crowns embodying {usp}, "
                f"staged inside a minimalist modernist brutalist gallery, {preset['materials']}, "
                f"dramatic high-contrast edge rim light, {preset['lighting']}, "
                f"ample clean negative space for brand slogan at the top, "
                f"{preset['camera']} --ar {aspect_ratio} --v 6.1 --stylize 200 "
                f"--no text, letters, watermarks, logo, blurry, extra limbs, low resolution"
            ),
            "flux_prompt": (
                f"Dynamic commercial key visual of {product} captured in high-speed kinetic freeze. "
                f"Particles and fluid waves are frozen in mid-air around the product to illustrate {usp}. "
                f"Textures include {preset['materials']}. Lit by {preset['lighting']}. "
                f"Clean negative space at the top for branding."
            )
        }
    ]

    return {
        "product": product,
        "usp": usp,
        "category": preset["name"],
        "aspect_ratio": aspect_ratio,
        "concepts": concepts
    }

def main():
    parser = argparse.ArgumentParser(description="Generate commercial advertising key visual campaigns.")
    parser.add_argument("--product", required=True, help="Product name or description")
    parser.add_argument("--usp", required=True, help="Unique Selling Proposition / Core Benefit")
    parser.add_argument("--category", default="tech", choices=list(INDUSTRY_PRESETS.keys()), help="Industry category")
    parser.add_argument("--ar", default="3:4", help="Aspect ratio (e.g. 3:4, 4:5, 16:9, 9:16, 1:1)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()
    data = generate_campaign(args.product, args.usp, args.category, args.ar)

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    print(f"# 商业广告提案：{data['product']}")
    print(f"- **行业品类**：{data['category']}")
    print(f"- **核心卖点 (USP)**：{data['usp']}")
    print(f"- **主推画幅**：{data['aspect_ratio']}\n")

    for i, c in enumerate(data['concepts'], 1):
        print(f"## 方案 {chr(64+i)}：{c['title']} ({c['type']})")
        print(f"- **广告标语**：{c['slogan_zh']} / *{c['slogan_en']}*")
        print(f"- **超现实隐喻**：{c['metaphor']}")
        print(f"- **置景与留白**：{c['staging']} | **留白区**：{c['copy_space']}")
        print(f"\n**Midjourney v6.1 Prompt:**\n```text\n{c['mj_prompt']}\n```")
        print(f"\n**Flux.1 Prompt:**\n```text\n{c['flux_prompt']}\n```\n")

if __name__ == "__main__":
    main()
