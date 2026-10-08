---
name: ad-surreal-skill
description: Directly generate and render high-concept commercial advertising key visuals (KV), product posters, and portraits featuring a signature minimalist aesthetic with vast negative space, ultra-pale neutral backgrounds, or bold graphic color-blocking. Generates and renders final image files directly in the chat rather than returning text prompts.
metadata:
  short-description: Minimalist negative-space commercial KV & image generator
---

# Ad Surreal — Minimalist Negative-Space Commercial Generator

`ad-surreal-skill` 是专为高概念商业广告大片（Commercial KV）、产品海报与先锋视觉设计的**通用直接生图技能**。

**核心视觉标志 (Signature Aesthetic)**：
- **背景极简**：使用**极淡单一色彩**（暖雪花白、淡牡蛎灰、柔和米胚）或**高阶强烈撞色**（克莱因蓝/暖杏、墨黑/酸绿）；
- **大面积留白**：**以负空间作为背景本身**，画面 65%–80% 为纯净负空间，留足视觉呼吸感与排版安全区；
- **雕塑感主体**：产品或人物置于偏心黄金分割点，配合细腻克制的地面接触微阴影与哈苏中画幅影棚光；
- **直接生图交付**：直接生成图片并在对话中内联展示，绝不向用户倾倒无用的提示词文本。

---

## 资源路由 (Supporting References)

- **`references/minimal-negative-space-style.md`**：**核心视觉规范**（极淡单色天幕、高阶撞色色块、大面积留白构图比例与接触阴影）。
- **`references/portrait-blueprints.md`**：人像大片标准（微孔真实皮肤质感、次表面散射 SSS、克制高级神态）。
- **`references/metaphor-archetypes.md`**：五大超现实隐喻母题（尺度错位、物性反转、失重悬浮与子弹时间、异质共生、通感显影）。
- **`references/industry-blueprints.md`**：垂直行业工业级材质与布光蓝图。

---

## 自动化生图工作流 (Automated Workflow)

### 第一步：视觉风格对齐
根据需求或用户意向，自动将画面锚定在两种标志性背景分支之一：
1. **淡色纯净分支 (Pale Monochromatic)**：超淡暖雪白 / 淡灰无缝影棚天幕，75% 纯净负空间；
2. **大胆撞色分支 (Graphic Color Blocking)**：几何双色撞色（如钴蓝配暖杏、深黑配酸橙），70% 平面视觉负空间。

### 第二步：直接生成并保存
运行 `scripts/generate_image.py` 直接生成高清图片，保存至 `output/campaigns/{slug}/kv.jpg`：
```bash
python3 /Users/wxqdoit/Documents/dev/ad-surreal-skill/scripts/generate_image.py \
  "<enhanced_prompt>" \
  --out "/Users/wxqdoit/Documents/dev/ad-surreal-skill/output/campaigns/{slug}/kv.jpg"
```

### 第三步：对话内联交付
在回复中直接使用 Markdown 绝对路径渲染展示图片，附带极简的 1–2 句概念与色调说明：
```markdown
![作品标题](/Users/wxqdoit/Documents/dev/ad-surreal-skill/output/campaigns/{slug}/kv.jpg)
```
