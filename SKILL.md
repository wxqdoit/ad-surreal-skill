---
name: ad-surreal-skill
description: Directly generate and render high-concept commercial advertising key visuals (KV), product posters, and fashion portraits across diverse signature styles (Haute Couture, Pure Negative-Space Minimalist, Modern Color-Blocking, Cinematic Noir, Sunlit Caustics, Cyber Photon, and Botanical Surrealism). Directly outputs and renders final image files in the chat rather than returning text prompts.
metadata:
  short-description: Universal commercial KV & fashion image generator with curated styles
---

# Ad Surreal — Multi-Style Commercial & Fashion Generator

`ad-surreal-skill` 是专为高概念商业广告大片（Commercial KV）、产品海报与高端时尚人像设计的**通用直接生图技能**。

---

## 多元风格矩阵 (Curated Style Matrix)

技能内置了全球顶级商业与时尚大片的核心视觉风格（详见 `references/style-catalog.md`）：

1. **`haute-couture` · 法式高定静奢风 (Haute Couture & Quiet Luxury)**：
   - 温暖燕麦/米白中性色调、极简哑光几何立方台座、抓褶轻纱/丝绸晚礼服、优雅低盘发、左上角微型法文衬线排版（`LUMIÈRE ÉTÉ`）。
2. **`minimal-void` · 科技极简纯粹留白风 (Pure Negative-Space Minimalist)**：
   - 暖雪花白/淡牡蛎灰天幕、75% 极度留白作为背景、偏心雕塑感主体、细腻接触微阴影、瑞士无衬线排版。
3. **`color-block` · 先锋现代几何撞色风 (Swiss Modern Graphic Color-Blocking)**：
   - 高饱和几何色块分割（克莱因蓝+暖杏橙、深黑+酸绿）、强平面视觉张力、70% 负空间。
4. **`cinematic-noir` · 电影级暗调戏剧光影风 (Cinematic Chiaroscuro & Film Noir)**：
   - 伦勃朗强戏剧侧光、深邃墨黑低调阴影、微胶片颗粒感、深沉叙事张力与贵族质感。
5. **`sunlit-caustics` · 地中海日光焦散风 (Mediterranean Sunlit Caustics)**：
   - 温暖金晖斜阳、天然水波焦散光斑、粗粝洞石台座、透亮原生水光肌与自然度假奢华感。
6. **`cyber-photon` · 先锋赛博光子与暗夜霓虹风 (Midnight Cyber & Luminous Photon)**：
   - 深邃午夜蓝黑基底、双色冷暖极细轮廓光、流动光子光轨、高科技穿戴与暗调奢华。
7. **`botanical-surreal` · 空灵植物超现实风 (Ethereal Botanical Surrealism)**：
   - 人物/产品与水晶微缩花卉、悬浮露珠无界交融、如梦似幻的自然诗意。

---

## 资源路由 (Supporting References)

- **`references/style-catalog.md`**：**完整多元商业风格库**（每种风格的调色板、台座置景、光影、人物服饰与角标排版）。
- **`references/minimal-negative-space-style.md`**：极简留白与负空间核心设计规范。
- **`references/portrait-blueprints.md`**：人像大片标准（微孔真实皮肤质感、次表面散射 SSS、克制高级神态）。
- **`references/metaphor-archetypes.md`**：五大超现实隐喻母题（尺度错位、物性反转、失重悬浮与子弹时间、异质共生、通感显影）。

---

## 自动化生图工作流 (Automated Workflow)

### 第一步：风格匹配或由用户指定
- 若用户上传参考图或指定风格（如法式高定、极简留白、撞色等），直接匹配对应风格预设；
- 若未指定，根据产品或人像品类智能推荐最具商业张力的风格。

### 第二步：直接生成并保存
运行 `scripts/generate_image.py` 直接生成高清图片，保存至 `output/campaigns/{slug}/kv.jpg`：
```bash
python3 /Users/wxqdoit/Documents/dev/ad-surreal-skill/scripts/generate_image.py \
  "<subject_or_prompt>" \
  --style haute-couture \
  --out "/Users/wxqdoit/Documents/dev/ad-surreal-skill/output/campaigns/{slug}/kv.jpg"
```

### 第三步：对话内联交付
在回复中直接使用 Markdown 绝对路径渲染展示图片，附带极简的 1–2 句概念与色调说明：
```markdown
![作品标题](/Users/wxqdoit/Documents/dev/ad-surreal-skill/output/campaigns/{slug}/kv.jpg)
```
