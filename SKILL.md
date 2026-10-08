---
name: ad-surreal-skill
description: Generate high-concept commercial advertising campaigns, surreal key visuals (KV), brand posters, and visual metaphor prompts for 3C tech, luxury, beauty, athletic, automotive, and FMCG brands. Use this skill to translate product USPs and marketing objectives into Cannes-grade surreal visual metaphors, studio cinematography, negative copy space layouts, and production-ready Midjourney/Flux prompts.
metadata:
  short-description: High-concept commercial advertising & surreal KV campaigns
---

# Ad Surreal — Commercial Advertising & Key Visual Engine

`ad-surreal-skill` 是专为高概念商业广告大片（High-Concept Commercial Campaigns）、品牌主视觉（Key Visual / KV）、户外大牌海报及视觉隐喻提示词设计的顶尖创意总监级技能。

本技能将普通的产品陈列升华为具备**戛纳创意奖（Cannes Lions）质感**的超现实视觉大片：**以产品核心卖点（USP）为支点，驱动超现实视觉隐喻（Visual Metaphor），预留商业排版留白（Copy Space），并生成工业级 Midjourney 与 Flux 提示词**。

---

## 核心法则 (The 4 Golden Rules)

1. **卖点即物理法则 (USP as Law of Physics)**：超现实元素绝非盲目的奇幻拼贴，每一个超现实奇观都必须是产品卖点（如“极致降噪”、“轻若鸿毛”、“瞬间冷凝”、“深层渗透”）的戏剧化实体外化。
2. **拒绝平庸静物 (Concept > Pixel)**：普通产品摆拍是电商白底图，不是商业大片。必须引入冲突、张力与超现实意象。
3. **商业排版留白工程 (Copy Space Engineering)**：商业海报必须预留文案区（Headline / Slogan / Body Copy / Logo 区域）。提示词中必须显式定义负空间（Negative Space）与构图偏心。
4. **影棚级光学与微米质感 (Cinematography & Macro Textures)**：采用哈苏中画幅相机语言、Profoto 影棚布光系统、水波焦散（Caustics）、次表面散射（SSS）与宏观建筑置景，拒绝塑料感与廉价 3D 渲染。

---

## 资源路由 (Supporting References)

根据任务深入度按需阅读对应模块：
- **`references/metaphor-archetypes.md`**：五大经典超现实商业视觉隐喻母题（尺度错位、物性反转、失重悬浮与子弹时间、异质共生与矛盾空间、感官通感力场显影）。
- **`references/industry-blueprints.md`**：六大垂直行业（3C数码、奢品美妆、运动户外、汽车出行、快消饮料、智能家居）的专属材质、布光、配色与参数蓝图。
- **`references/prompt-grammar.md`**：7 层工业级商业 Prompt 黄金公式、排版留白控制与规避词（Negative Prompts）。
- **`references/campaign-framework.md`**：4A 广告公司提案结构、大创意（The Big Idea）推导与多方案提案卡片规范。

---

## 工作流 (Execution Workflow)

### 第一步：简报解析与策略洞察 (Strategic Brief Deconstruction)
从用户输入中提取或推导核心策略四要素：
1. **产品与品类 (Product & Category)**：明确产品形态与行业属性。
2. **核心卖点 (USP / Core Benefit)**：提炼出最核心的 1 个差异化卖点（如“超强吸力”、“全天候防水”、“零延迟响应”）。
3. **目标受众与心智触点 (Audience Insight)**：用户在使用该产品时的向往状态或情感共鸣。
4. **沟通大创意 (The Big Idea & Slogan)**：撰写具有穿透力的中英双语主标语（Punchline）。

### 第二步：三维超现实隐喻推导 (Tri-Concept Ideation)
为用户提供 **3 套差异化的超现实视觉方案**，分别匹配不同的隐喻母题（参考 `references/metaphor-archetypes.md`）：
- **方案 A (尺度奇观 / 宏观巨物或微观宇宙)**：将产品作为地标自然景观，或微观结构宏大化。
- **方案 B (物性反转 / 材质炼金与流体晶变)**：刚柔互换、液体凝固为水晶雕塑、生物机械共生。
- **方案 C (失重瞬态 / 爆炸解构或矛盾置景)**：精密零件悬浮解构、高速子弹时间碰撞、极简美术馆与原始自然并置。

### 第三步：生成 7 层工业级提示词 (Prompt Compilation)
对每套方案，严格按照 `references/prompt-grammar.md` 编制工业级生图提示词：
- 包含商业级别、核心主体、超现实动作、置景空间、微米材质、影棚灯光、**排版留白声明**及技术参数。
- 提供 **Midjourney v6.1** 结构化提示词（带 `--ar`, `--v 6.1`, `--stylize` 等参数及 `--no` 规避词）。
- 提供 **Flux.1** 自然语言高保真摄影提示词。

### 第四步：输出专业提案卡片 (Proposal Presentation)
严格按照 `references/campaign-framework.md` 格式向用户交付：
- 策略概览（产品、USP、受众洞察、Big Idea）。
- 方案 A / B / C 详细卡片（标语、隐喻机制、置景与光影、留白规划、Midjourney Prompt、Flux Prompt）。
- 商业物料延展建议（主推画幅、字体排版指南、多媒介适配）。

### 第五步：生图执行与打磨 (Optional Image Generation & Refinement)
- 当环境中具备生图能力（如可用 `imagegen` 技能或插件）且用户明确要求出图时，调用生图工具为最推荐的方向渲染概念大片。
- 若用户选定某一方案要求深化，可进一步展开为多画幅全套物料（如 3:4 社交海报、16:9 发布会大屏、9:16 移动端开屏）。
