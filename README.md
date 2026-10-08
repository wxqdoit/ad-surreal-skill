# Ad Surreal (`ad-surreal-skill`)

> **High-Concept Commercial Advertising & Key Visual Campaign Engine**  
> 专为商业高概念广告大片、品牌主视觉（Key Visual / KV）、户外大牌海报及视觉隐喻提示词设计的顶尖创意总监级 Codex 技能。

---

## 🌟 核心价值与设计哲学

普通 AI 生图往往停留在“产品白底图”或“无目的的科幻拼贴”，存在三大痛点：
1. **画面太满**：没有为商业文案、Headline、Slogan 和品牌 Logo 预留排版空间（Copy Space）。
2. **缺乏概念**：平铺直叙，没有能够击中消费者心智的**视觉隐喻（Visual Metaphor）**。
3. **质感廉价**：充斥着游戏 CG 塑料高光或杂乱几何噪点，达不到 4A 广告公司千万元级制作标准。

**`ad-surreal-skill` 确立了 4 大商业广告铁律：**
- **卖点即物理法则 (USP as the Law of Physics)**：超现实元素是产品核心卖点（如“极致降噪”、“轻若鸿毛”、“瞬间冷凝”、“深层渗透”）的戏剧化实体外化。
- **概念重于像素 (Concept > Pixel)**：没有视觉隐喻的画面只是普通静物摆拍，只有高概念隐喻才能形成具备戛纳创意奖（Cannes Lions）质感的破圈大片。
- **商业排版留白工程 (Copy Space Engineering)**：在 Prompt 语法中显式定义负空间（Negative Space）与偏心构图，严格预留排版区域。
- **工业级摄影与渲染质感 (Cinematography & Micro-optics)**：深度整合哈苏中画幅相机语言、Profoto 影棚布光系统、水波焦散（Caustics）、次表面散射（SSS）与宏观建筑置景。

---

## 📁 目录架构 (Architecture)

```text
ad-surreal-skill/
├── SKILL.md                          # 技能入口与工作流核心调度
├── README.md                         # 技能完整文档与使用指南
├── agents/
│   └── openai.yaml                   # Codex 界面与交互定义
├── references/
│   ├── metaphor-archetypes.md        # 5 大超现实商业视觉隐喻母题
│   ├── industry-blueprints.md        # 6 大垂直行业工业级质感与布光蓝图
│   ├── prompt-grammar.md             # 7 层工业级 Prompt 黄金公式与留白规范
│   └── campaign-framework.md         # 4A 广告公司创意提案卡与推导框架
└── scripts/
    ├── generate_campaign.py          # 独立命令行提案生成与模板测试工具
    └── validate_skill.py             # 技能完整性与语法校验脚本
```

---

## 🎨 五大超现实视觉隐喻母题 (`references/metaphor-archetypes.md`)

1. **尺度错位与极端微缩 / 宏观 (Scale Distortion)**
   - *巨物地标*：将产品放大为百米巨构，矗立于峡谷极境，微小的人物或飞鸟衬托浩瀚统治力。
   - *微观宇宙*：将芯片晶体管、护肤分子、织物纤维转译为繁华的流光微观都市。
2. **物性反转与材质炼金 (Material Alchemy)**
   - *刚柔互换*：坚硬的钛合金、陶瓷机身化作如水银般的液态丝绸在空中翻折。
   - *形态晶变*：迸发的水花与香水在微秒内凝固成晶莹剔透的水晶钻石雕塑。
   - *生物机械共生*：芯片电路板生长出娇艳的高定花卉与发光苔藓。
3. **失重悬浮与瞬态动力学 (Zero-G Levitation & Kinetic Freeze)**
   - *精密爆炸解构*：在零重力场中将声学腔体、光学镜片有序层层悬停展开。
   - *高速子弹时间定格*：1/8000s 凝固能量粉末爆破、液滴皇冠碰撞瞬间。
4. **异质共生与矛盾空间 (Impossible Juxtaposition)**
   - *极简画廊融合野性自然*：清水混凝土展厅地面长出原始红杉林与静止水镜。
   - *气候极境对抗*：极地冰川与沙漠绿洲在画面中央完美分割并置。
5. **感官实体化与隐形力场显影 (Synesthesia & Force Field)**
   - *主动降噪显影*：降噪被具象化为一个抚平外界喧嚣声波的透明极光能量罩。
   - *极致轻盈*：数吨重的大理石雕塑轻盈平衡在一片天鹅绒羽毛之上。

---

## 🏭 六大行业视觉蓝图 (`references/industry-blueprints.md`)

- **3C 数码与极客计算**：钛金属、阳极氧化铝、蓝宝石玻璃、双色微弱冷暖轮廓光、极简深空虚境。
- **奢华美妆、香氛与护肤**：重工厚底水晶、水波焦散光、晨曦丁达尔光束、次表面散射 (SSS)、洞石水景。
- **专业运动、跑鞋与硬核户外**：外露编织碳板、超临界发泡、硬质逆光轮廓、火山碎石、动能环。
- **高端汽车与未来出行**：多层液态金属漆面、锻造碳纤维扰流板、湿滑路面倒影、空气动力学光带。
- **食品饮料与精酿汽水**：冰霜凝露水珠、晶莹多面体冰块、果汁微型海啸、高饱和透光清爽日光。
- **智能家居与生活方式**：白橡木、洞石、羊羔绒、大落地窗柔和漫射日光、侘寂极简挑高空间。

---

## 📐 7 层工业级 Prompt 黄金公式 (`references/prompt-grammar.md`)

```text
[L1: Commercial Hero Subject] 商业定位与核心主体
+ [L2: Surreal Metaphor Action] 超现实隐喻动作与戏剧态
+ [L3: Environment & Staging] 置景空间与环境基底
+ [L4: Materials & Micro-optics] 微米级材质与光学反射
+ [L5: Lighting & Mood] 商业影棚布光与氛围
+ [L6: Composition & Copy Space] 构图层级与文案留白区（核心）
+ [L7: Camera & Parameters] 摄影器材、渲染引擎与技术参数
```

---

## 🚀 快速上手与使用示例

### 1. 在 Codex 对话中调用
输入任意产品、卖点或概念需求：
> *"帮我的新款钛合金主动降噪耳机设计一套超现实商业 KV 方案，突出'纯净如深海的静谧'。"*

技能将自动推导：
- **策略概览**（品类、USP、受众洞察、Campaign Big Idea & Slogan）
- **3 套差异化超现实方案**（尺度奇观、材质炼金、失重解构）
- **Midjourney v6.1 与 Flux.1 即用型提示词**（包含排版留白指令与负向词）
- **多画幅适配建议**（3:4 社交、16:9 大牌、9:16 开屏）

### 2. 本地命令行工具测试
```bash
# 生成 3C 耳机提案
python3 scripts/generate_campaign.py \
  --product "Aura Pro Wireless Headphones" \
  --usp "Pure Deep-Sea Active Noise Cancellation" \
  --category tech \
  --ar 3:4

# 生成奢华香水提案并输出 JSON
python3 scripts/generate_campaign.py \
  --product "L'Ombre Nobilis Perfume" \
  --usp "Instant Floral Crystallization" \
  --category luxury \
  --json
```

### 3. 校验技能完整性
```bash
python3 scripts/validate_skill.py
```
