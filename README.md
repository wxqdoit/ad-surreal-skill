# Ad Surreal (`ad-surreal-skill`)

> **Direct Commercial Advertising Key Visual & Surreal Campaign Generator**  
> 专为商业高概念广告大片、品牌主视觉（Key Visual / KV）与超现实视觉隐喻海报设计的**直接生图技能**。

---

## 🌟 核心定位：从“提示词草案”到“直接生图交付”

传统的 AI 创意工具大多只能输出一段文本提示词，需要用户手动复制到生图软件调试。  
**`ad-surreal-skill` 全面升级为“直接生图技能”**：
- **策略到大片一体化**：接收产品与卖点输入 -> 自动推导 4A 创意大概念（Big Idea）与视觉隐喻 -> 编译 7 层工业级提示词 -> **直接调用生图工具渲染高清广告大图**。
- **排版留白工程 (Copy Space Engineering)**：在画面中严控留白区（Negative Space），预留商业文案、Headline、Slogan 与 Logo 空间，拒绝堆砌无处排版。
- **工业级摄影与渲染质感**：结合哈苏中画幅相机语言、Profoto 影棚布光系统、水波焦散（Caustics）、次表面散射（SSS）与微米级材质，杜绝廉价塑料感。

---

## 📁 目录架构 (Architecture)

```text
ad-surreal-skill/
├── SKILL.md                          # 技能入口与直接生图工作流调度
├── README.md                         # 技能完整文档与使用指南
├── agents/
│   └── openai.yaml                   # Codex 界面与交互定义
├── references/
│   ├── metaphor-archetypes.md        # 5 大超现实商业视觉隐喻母题
│   ├── industry-blueprints.md        # 6 大垂直行业工业级质感与布光蓝图
│   ├── prompt-grammar.md             # 7 层工业级 Prompt 黄金公式与留白规范
│   └── campaign-framework.md         # 4A 广告公司创意提案卡与推导框架
├── scripts/
│   ├── generate_ad_image.py          # 核心生图与资产归档执行工具
│   ├── generate_campaign.py          # 提案文本与多方案测试工具
│   └── validate_skill.py             # 技能完整性与语法校验脚本
└── output/
    └── campaigns/                    # 生成的商业广告海报与 Prompt 资产归档
        └── {slug}/
            ├── kv.png                # 渲染生成的高清商业海报
            └── prompt.md             # 策略与工业级提示词归档
```

---

## 🎨 五大超现实视觉隐喻母题 (`references/metaphor-archetypes.md`)

1. **尺度错位与极端微缩 / 宏观 (Scale Distortion)**：巨物化产品如百米神庙矗立自然极境，或将芯片晶体管转译为流光微观都市。
2. **物性反转与材质炼金 (Material Alchemy)**：钛合金机身如液态金属丝绸飘扬，或水花在空气中凝固成晶莹水晶雕塑。
3. **失重悬浮与瞬态动力学 (Zero-G Levitation & Kinetic Freeze)**：声学零件在零重力空间整齐悬浮解构，或 1/8000s 高速定格能量爆破瞬间。
4. **异质共生与矛盾空间 (Impossible Juxtaposition)**：极简清水混凝土画廊内穿透高山水镜与原始森林，打造静谧的超脱感。
5. **感官实体化与隐形力场显影 (Synesthesia & Force Field)**：将降噪转化为抚平喧嚣的深蓝液态能量罩，或将算力转化为流光溢彩的光子隧道。

---

## 🚀 使用方式

### 1. 在 Codex 对话中调用
输入产品形态与核心卖点：
> *"使用 `$ad-surreal-skill` 直接为一款全新钛合金主动降噪耳机生成商业 KV，核心卖点为'纯净如深海的静谧'。"*

技能将自动：
1. 提炼策略洞察与主标语（Campaign Slogan & Big Idea）。
2. 匹配最具视觉冲击力的超现实隐喻。
3. 执行生图并将作品保存至 `output/campaigns/{slug}/kv.png`。
4. 在对话中直接以 Markdown 渲染展示图片，并附带 4A 提案卡片与复用提示词。

### 2. 命令行独立执行生图
```bash
# 生成钛合金降噪耳机商业 KV（含 prompt.md 保存）
python3 scripts/generate_ad_image.py \
  --product "Titanium ANC Headphones" \
  --usp "Pure Deep-Sea Silence" \
  --category tech \
  --metaphor scale \
  --ar 3:4

# 加上 --generate 参数直接调用生图引擎渲染图像
python3 scripts/generate_ad_image.py \
  --product "Titanium ANC Headphones" \
  --usp "Pure Deep-Sea Silence" \
  --category tech \
  --metaphor scale \
  --ar 3:4 \
  --generate
```

### 3. 校验技能完整性
```bash
python3 scripts/validate_skill.py
```
