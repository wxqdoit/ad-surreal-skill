---
name: ad-surreal-skill
description: Directly generate high-concept commercial advertising key visuals (KV), surreal brand campaign images, and visual metaphor posters for products. Use this skill when asked to generate commercial ad images, brand KVs, product launch posters, or visual metaphor campaigns, rendering the final high-end visual directly in the workspace.
metadata:
  short-description: Directly generate surreal commercial advertising KVs & campaign images
---

# Ad Surreal — Direct Commercial KV & Campaign Generator

`ad-surreal-skill` 是专为高概念商业广告大片（High-Concept Commercial Campaigns）、品牌主视觉（Key Visual / KV）与视觉隐喻海报设计的**直接生图技能**。

本技能的核心目标是**直接输出渲染完成的商业级视觉大片**：以产品核心卖点（USP）驱动超现实视觉隐喻（Visual Metaphor），预留商业排版留白（Copy Space），调用生图引擎生成高清大图，并内联渲染交付。

---

## 核心法则 (The 4 Golden Rules)

1. **直接生图交付 (Direct Visual Output)**：不仅输出方案和提示词，更要直接调用生图工具生成最终图像，并在对话中使用 Markdown 绝对路径渲染展示：`![Commercial KV](/absolute/path/to/kv.png)`。
2. **卖点即物理法则 (USP as Law of Physics)**：超现实元素是产品核心卖点（如“极致降噪”、“轻若鸿毛”、“瞬间冷凝”、“深层渗透”）的戏剧化实体外化，拒绝无目的的平庸静物或盲目奇幻拼贴。
3. **商业排版留白工程 (Copy Space Engineering)**：商业海报必须预留文案区（Headline / Slogan / Logo 区域）。提示词中显式定义负空间（Negative Space）与偏心构图。
4. **工业级影棚质感 (Cinematography & Micro-optics)**：采用哈苏中画幅相机语言、Profoto 影棚布光系统、水波焦散（Caustics）、次表面散射（SSS）与微米级材质，杜绝廉价塑料 CG 感。

---

## 资源路由 (Supporting References)

根据任务深入度按需查阅：
- **`references/metaphor-archetypes.md`**：五大超现实隐喻母题（尺度错位、物性反转、失重悬浮与子弹时间、异质共生、通感显影）。
- **`references/industry-blueprints.md`**：六大行业（3C数码、奢品美妆、运动户外、汽车出行、快消饮料、智能家居）的专属材质、布光、配色蓝图。
- **`references/prompt-grammar.md`**：7 层工业级商业 Prompt 黄金公式、排版留白控制与规避词（Negative Prompts）。
- **`references/campaign-framework.md`**：4A 广告公司提案结构、大创意推导与提案卡片规范。

---

## 工作流 (Direct Generation Workflow)

### 第一步：策略与隐喻推导 (Strategy & Metaphor Selection)
1. 从用户输入中提取或推导核心策略：
   - **产品与品类**：明确产品形态（如钛合金降噪耳机、折叠屏手机、高定香水、竞速跑鞋）。
   - **核心卖点 (USP)**：提炼出最核心的 1 个差异化卖点（如“深海级降噪”、“瞬间回弹”、“轻若丝绒”）。
   - **大创意 (Big Idea & Slogan)**：提炼有穿透力的中英双语主标语。
2. 匹配最佳超现实视觉隐喻（参考 `references/metaphor-archetypes.md`）：
   - 若用户已指定方向，直接采用；
   - 若用户未指定，默认选用最具视觉冲击力的母题（如 3C 耳机优先推荐深海地标或水滴结界），并简要说明隐喻逻辑。

### 第二步：编译 7 层工业级提示词 (Prompt Compilation)
严格按照 `references/prompt-grammar.md` 编制工业级生图提示词：
- 结构：商业级别 + 核心主体 + 超现实动作 + 置景空间 + 微米材质 + 影棚布光 + 排版留白声明 + 摄影参数。
- 自动生成并归档提示词文件至 `output/campaigns/{slug}/prompt.md`。

### 第三步：直接执行生图 (Direct Image Generation)
1. **生图工具调用**：
   - 优先使用可用生图工具生成图像（如内置 `image_gen` 或通过脚本 `scripts/generate_ad_image.py --generate`）；
   - 输出图像路径统一规范为：`output/campaigns/{slug}/kv.png`；
   - 商业海报默认画幅比例：`3:4`（社交与杂志海报）或 `16:9`（发布会与大牌）。
2. **环境兜底策略**：
   - 若当前运行环境缺少可用生图接口或 API 密钥受限，完整保存 `prompt.md`，并在回答中展示完整的提案卡片、Midjourney/Flux 生图提示词及一键生图命令，绝不虚构本地图片路径。

### 第四步：视觉交付与画板呈现 (Visual Delivery & Board Presentation)
在最终回复中，完整呈现以下内容：
1. **生成的商业大片**：成功生图后，直接使用 Markdown 绝对路径渲染：
   ```markdown
   ![Commercial Key Visual](/absolute/path/to/output/campaigns/{slug}/kv.png)
   ```
2. **4A 商业提案卡片**：
   - **品牌产品与 USP**
   - **Campaign Big Idea & Slogan**
   - **超现实隐喻机制解析**（说明为何此隐喻能击穿消费者心智）
   - **版面与留白指引**（Copy Space 区域说明及字体搭配建议）
3. **可复用工业级 Prompt 卡片**：
   - 包含 Midjourney v6.1 完整参数提示词及 Flux.1 自然语言提示词，方便外部二次精修或导出。
