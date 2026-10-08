# 商业广告级 Prompt 语法与留白工程 (Prompt Grammar & Copy Space)

AI 生图在商业广告落地时面临的最大痛点：**画面太满无处排版、产品质感像廉价游戏CG、元素堆砌失去主视觉焦点**。

顶级商业广告 Prompt 必须具备**分层严密性**与**排版留白意识**。本语法体系专为 Midjourney v6.1 与 Flux.1 设计。

---

## 7 层工业级商业 Prompt 黄金公式

```text
[层级 1: 商业定位与主视觉产品]
+ [层级 2: 超现实隐喻动作与戏剧态]
+ [层级 3: 置景空间与环境基底]
+ [层级 4: 微米级材质与光学反射]
+ [层级 5: 商业影棚布光与氛围]
+ [层级 6: 构图层级与文案留白区]
+ [层级 7: 摄影器材、渲染引擎与技术参数]
```

### 层级详解与填空规范

| 层级 | 模块名称 | 核心作用 | 英文规范词示例 |
|---|---|---|---|
| **L1** | **Commercial Hero Subject** | 确立广告级别与产品主体形态 | `Award-winning commercial key visual, hero shot of a minimalist matte titanium noise-cancelling headphone...` |
| **L2** | **Surreal Metaphor Action** | 注入核心卖点对应的超现实物理动作 | `...suspending in zero-gravity while exterior chaotic soundwaves dissolve into smooth crystalline water ripples...` |
| **L3** | **Environment & Staging** | 构筑极简或史诗感的背景舞台 | `...set in a vast minimalist architectural concrete pavilion opening to a misty alpine sunrise...` |
| **L4** | **Materials & Micro-optics** | 确保工业级物理真实感 | `...macro textures of anodized metallic finish, sapphire glass glints, refractive caustics, subtle subsurface scattering...` |
| **L5** | **Lighting & Mood** | 商业影棚灯位安排 | `...lit by Profoto softbox key light, dramatic crisp cyan edge rim light, soft diffuse fill, pristine contrast...` |
| **L6** | **Composition & Copy Space** | **最关键：预留设计师文案与Logo排版区** | `...off-center composition, ample clean negative space on the top-left for brand headline and typography...` |
| **L7** | **Camera & Parameters** | 器材标准与模型渲染参数 | `...shot on Hasselblad H6D-100c, 85mm f/8 commercial lens, Octane 3D render fidelity, 8k resolution --ar 3:4 --v 6.1 --stylize 250` |

---

## 商业留白区 (Copy Space / Negative Space) 控制指南

在商业设计中，“留白”不是空白，而是高阶审美与信息载体。必须在 Prompt 中显式声明排版留白区域：

### 1. 顶部留白 (Top Negative Space) - 最适合海报/社交卡片
- **适用画幅**：`--ar 3:4`, `--ar 4:5`
- **使用场景**：主标题（Headline）居顶，产品主体在画面中下部或黄金分割点。
- **Prompt 语句**：
  `"clean minimalist gradient background at the upper third, leaving ample generous negative space at the top for advertising copy and brand headline"`

### 2. 左侧 / 右侧留白 (Side Negative Space) - 最适合横版大牌与官网 Banner
- **适用画幅**：`--ar 16:9`, `--ar 21:9`
- **使用场景**：户外立柱看板、发布会大屏、官网 Hero 图。左文右图或左图右文。
- **Prompt 语句**：
  `"hero product positioned dynamically on the right half, with a spacious, uncluttered negative space across the left half reserved for editorial typography"`

### 3. 中心极简呼吸感 (Central Floating Breathe Room)
- **适用画幅**：`--ar 1:1`
- **使用场景**：单品精修、电商封面、高端画册局部。
- **Prompt 语句**：
  `"centered floating sculptural composition surrounded by an airy, pristine minimalist void with soft vignetting"`

---

## 商业画幅比例矩阵 (Aspect Ratios)

| 画幅比例 | 目标媒介 | 商业物料形态 | 参数 |
|---|---|---|---|
| **3:4** | 社交主图 / 杂志内页 | 小红书商业封面、微信图文大卡、时尚杂志整版海报 | `--ar 3:4` |
| **4:5** | 国际社交媒体 | Instagram 竖版广告、Facebook Feed、品牌型录 | `--ar 4:5` |
| **9:16** | 移动全屏 | App 开屏广告、抖音/小红书全屏故事 (Stories)、手机壁纸海报 | `--ar 9:16` |
| **16:9** | 宽幅商业大牌 | 发布会 Keynote 幻灯片、官网 Hero Banner、机场大灯箱 | `--ar 16:9` |
| **21:9** | 电影级超宽屏 | 高铁站全景巨幕、超宽户外 LED 屏、电影感片头 KV | `--ar 21:9` |
| **1:1** | 电商与单品方格 | 旗舰店方图、产品详情页第一屏、Instagram 方形展格 | `--ar 1:1` |

---

## 规避词与商业品控底线 (Negative Constraints)

商业广告绝对禁止以下 AI 常见瑕疵：
1. **禁止浮动乱码字**：AI 自带的无意义字母碎片严重破坏高级感。
2. **禁止廉价塑料高光 (Plastic Gloss)**：必须指明材质细节（如 `matte anodized`, `frosted glass`）以避免廉价 3D 感。
3. **禁止多主体混杂 (Visual Clutter)**：一个 KV 只能有 1 个 Hero Subject。

### Midjourney 负向控制：
```text
--no text, letters, watermarks, logo, blurry textures, low polygon, cheap plastic render, cluttered background, cartoon, oversaturated neon, extra floating debris
```

### Flux.1 负向与正向锚定：
在 Flux 提示中加入强调词：
`"commercial product photography, clean architectural space, crisp sharp focus, photorealistic studio lighting, no text, no watermarks, perfectly rendered geometry"`
