# Debug AI Writing

一个用于中文写作诊断、改写和质量检查的 Codex Skill。

它处理的不是“怎样骗过 AI 检测器”，而是实际写作问题：空泛套话、错误动宾关系、模板化结构、所有场景使用同一种语气、参考稿模仿失真、长文漏改，以及内外口径混用。

默认原则是：**先判断读者、场景和文体，再去 AI 味。** 专业方案保留策略感，白皮书保留证据和编辑空间，内部 SOP 保留执行效率，人物口播才使用口语和角色声音检查。不会把所有内容统一改成聊天语气。

## 主要能力

### 1. 场景与文体匹配

先识别材料给谁看、在什么渠道使用、读者需要做什么判断，再选择合适的表达尺度。支持：

- 客户方案、营销策划和销售材料
- 白皮书、案例、行业报告和研究结论
- 管理汇报、内部通知、会议跟进和 SOP
- 邮件、社交内容、演讲和个人文章
- 品牌口吻、个人口吻和参考稿风格对齐
- 创意方向、活动主题和内容选题筛选
- UGC/KOC/KOS、短视频口播和人物独白

不同文体分别加载对应的参考规则，不互相挪用。

### 2. 控制修改边界

把改稿分为四级：

- `L1`：只修病句、搭配和局部 AI 痕迹
- `L2`：重写语言，保留事实、结构和章节职责
- `L3`：重组结构或页面逻辑
- `L4`：补充分析、方法、案例或创意

“优化口径”“去 AI 味”默认按 `L2` 处理，不会未经允许把语言修改扩成方案重做。

### 3. 修复真正的 AI 写作问题

重点检查：

- 抽象动词加抽象名词，如“赋能增长”“激活心智”“构建闭环”
- 动词和宾语不自然，如“重新接回链路”“场景释放价值”
- 把结果伪装成动作，如“实现心智占位”“完成用户教育”
- 主体缺失，不知道谁在什么时间做什么
- 结论强于事实，把推测写成已验证结果
- 句式过度工整，段落、标题和结尾都使用同一模板
- 删除显眼套话后，又换成更隐蔽的精致空话

专业术语不是一律删除。只要它确实对应目标、机制、角色、阶段、指标或执行对象，就可以保留。

### 4. 整篇覆盖与修正传播

多页文档会先建立覆盖清单，再检查标题、正文、表格、图注、脚注、总结行和版本说明。用户指出一个问题后，会把它抽象成同类模式，扫描全文，而不是只修示例句。

### 5. 参考稿与个人口吻

使用参考稿前，先区分用户想借的是逻辑、结构、专业程度、节奏、措辞还是视觉组织，避免把“参考思路”误做成全文仿写。

个人口吻只在用户明确要求、提供样本或存在本地口吻档案时启用。开源版不默认携带任何人的私人写作风格。

### 6. 事实与内外口径

保留原稿中的事实、数字、证据等级和业务边界。对外材料会检查内部代号、内部指标、人名、未公开数据和只有团队内部才懂的表达，选择翻译成读者语言或删除。

## 场景参考

| 任务 | 主要检查 | 参考文件 |
| --- | --- | --- |
| 通用改写与生成 | 事实、结构、节奏、具体程度 | `references/rewrite-playbook.md` |
| 客户方案与策略稿 | 客户问题、判断、机制、执行证据 | `references/client-proposal-playbook.md` |
| 营销策划 | 目标、策略、角色、节点、平台与验收 | `references/marketing-strategy-register.md` |
| 白皮书与案例 | 行业价值、证据层级、可摘用表达 | `references/whitepaper-case-register.md` |
| 管理汇报与研究结论 | 决策信息、数据口径、风险和建议 | `references/executive-report-register.md` |
| 内部执行材料 | 责任、动作、时间、交付和异常处理 | `references/internal-ops-register.md` |
| 参考稿对齐 | 参考维度、风格合同和事实隔离 | `references/reference-style-calibration.md` |
| 人物与短视频脚本 | 人物声音、口语、画面分工和叙事结尾 | `references/ugc-persona-script-register.md` |

## 使用示例

普通改稿：

```text
[$debug-aiwriting] 帮我优化这段表达，保留事实和专业程度，只处理语言问题。
```

客户方案：

```text
[$debug-aiwriting] 检查这份营销方案的对客口径。不要改策略结构，重点修空话、假动作和不自然的动宾搭配。
```

参考稿对齐：

```text
[$debug-aiwriting] 参考这份 PDF 的专业表达和页面节奏，不照搬事实和结构，重写当前逐 P 稿。
```

长文覆盖：

```text
[$debug-aiwriting] 全文优化这份白皮书，标题、表格、图注和结尾都要检查，不要只改正文段落。
```

个人口吻：

```text
[$debug-aiwriting] 按我提供的文章提取口吻规律，再改这篇内容。不要套通用自媒体语气。
```

人物脚本：

```text
[$debug-aiwriting] 检查这批人物口播。隐藏人设标签后仍要听得出差异，不要让旁白复述画面，也不要为了自然感编造新细节。
```

## 自动审计工具

工具只负责定位风险，不代替人工判断。

### 多页文本覆盖

```bash
python3 scripts/audit_surfaces.py <文件路径> --output <清单.json>
```

用于盘点标题、表格、图注、总结行和高风险表达。用户明确否定某个词或短语时，可通过 `--term` 加入本轮扫描。

### DOCX 人物脚本库

```bash
python3 scripts/audit_ugc_scripts.py <脚本.docx> --output <报告.json>
```

需要比较原稿与改稿时：

```bash
python3 scripts/audit_ugc_scripts.py <改稿.docx> --baseline <原稿.docx> --output <报告.json>
```

该工具检查重复脚本、元数据缺口、结论公式、口吻集中、末格误删和疑似结尾拖尾。报告是复核线索，不会自动证明稿件已经自然。

## 安装

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/zhongky1995/debug-aiwriting.git ~/.codex/skills/debug-aiwriting
```

`debug-aiwriting` 是 Codex 使用的 skill 名称，`Debug AI Writing` 是展示名称。

## 自定义个人口吻

需要长期使用自己的表达习惯时，新建：

```text
local/personal-voice-profile.md
```

结构可参考 `references/personal-voice-profile-example.md`。`local/` 已加入忽略列表，不会随普通提交上传。

## 目录

```text
debug-aiwriting/
├── SKILL.md
├── agents/openai.yaml
├── scripts/
│   ├── audit_surfaces.py
│   ├── audit_ugc_scripts.py
│   └── test_audit_ugc_scripts.py
└── references/
    ├── rewrite-playbook.md
    ├── client-proposal-playbook.md
    ├── marketing-strategy-register.md
    ├── whitepaper-case-register.md
    ├── executive-report-register.md
    ├── internal-ops-register.md
    ├── reference-style-calibration.md
    ├── large-document-coverage.md
    ├── external-facing-check.md
    └── ugc-persona-script-register.md
```

## License

MIT
