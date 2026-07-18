# Debug AI Writing

一个用于中文写作去 AI 味的 Codex Skill。

它不是为了绕过检测器，而是帮助中文材料更像真实的人、品牌或咨询团队写出来：保留事实和场景，删掉空泛口号、白皮书腔、错误动宾搭配、结果伪装成动作，以及内外口径混用的问题。

## 适用场景

- 中文稿件去 AI 味、去模板感
- 客户方案、策略稿、白皮书、案例材料口径优化
- 个人口吻或品牌口吻迁移
- 对外材料的内部口径清理
- 创意方向筛选，避免只停留在概念词
- UGC、KOC、KOS、短视频口播和人物独白优化
- 多页文档、逐 P 稿、表格型方案的整篇覆盖检查
- 参考稿 / PDF / 旧版方案的表达口径对齐

## 核心判断

这个 skill 特别关注几类常见问题：

- 抽象动词 + 抽象名词：如“赋能增长”“激活心智”“释放价值”“构建闭环”
- 动宾关系不自然：如“内容完成用户教育”“场景释放产品价值”
- 主体缺失：句子没有说清楚谁在做动作
- 把结果写成动作：如“实现心智占位”“形成转化闭环”
- 不可验收的动词：无法回答“怎么做、谁来做、做完看到什么变化”
- 大面积改稿漏掉标题、表格、图注、版本说明等边角内容
- 去 AI 味时把专业策划语言误改成过于口语的执行说明
- 用户指出一个问题后，只改原句，没有检查全文同类表达
- “参考思路”和“参考表达”没有分开，导致结构、事实或语气被一起照搬
- 人设标签不同，人物实际说话时却仍像同一个文案作者
- 年龄、性别、服装和配音说明变了，实际台词的注意力、句式和判断方式没变
- 同一段口播在不同编号或不同人设下完整复制，审核时却只看到了标签变化
- 第一人称只负责总结意义、输出价值判断，缺少动作、感受和当下反应
- 旁白重复画面已经展示的信息，没有补充动机、背景或犹豫
- 每条口播都用感悟、反问或互动问题结尾
- 把“允许某个镜头无口播”误用成批量删结尾，导致最后一格从有内容变成空白
- 为了让人物“更真实”而编造原稿没有提供的动作、对话和生活细节

## UGC / 人设口播调试

这类脚本的问题通常不只是“第一人称太多”，而是**第一人称的功能过于单一**：不同人物都用“我”替画面总结意义、给出完整判断，最后再补一句感悟或反问。人设名称变了，背后的文案口吻没有变。

处理时会重点检查：

- **第一人称功能**：区分动作、感受、反应、犹豫、有限判断和空泛结论；优先删除没有场景支撑的结论。
- **去标签互换测试**：拿掉人设名称后，如果两段台词可以互换，说明人物没有真正写开。
- **人物语言系统**：分别定义人物在意什么、知道什么、不知道什么、句子长短、常用词和情绪温度，不靠方言或口头禅冒充人设。
- **台词盲测**：隐藏标题、人设、穿着、画面和配音说明，只读口播列。仍能大致判断人物类型和当下状态，才算真正写出口吻差异。
- **人物 × 场景双轴**：人物有稳定的注意力和表达习惯，场景决定当下语速和压力。不能把所有妈妈都写得忙乱，也不能把所有退休男性都写成慢生活散文。
- **重复口播检查**：不同编号下出现完全一致的整段台词，属于高优先级问题；换标题、服装或 TTS 音色不算改写。
- **画面 / 旁白分工**：画面交代动作和现场，旁白补充看不见的动机、前因、犹豫或后果，不复述画面。
- **结尾删除测试**：删掉强行升华或互动提问后，还要确认最后一个动作、现场话或画面回扣仍然存在；不能让脚本直接停在上一格。
- **结尾覆盖检查**：逐条比较原稿和改稿的最后一格。不得按人设、类别或编号范围批量清空；确实需要静默收尾时，要让画面完成叙事，并在制作格式中明确标记。
- **来源核对**：新增的动作、物件、对话、数字和人物反应必须能在原稿、人设卡或确认过的资料中找到依据。

### 2026-07-18 补强：清理“隐性 AI 味”

仅删除“我终于明白”“最重要的是”还不够。新版增加了四道验收：

- **隐性结论检查**：识别“路线由我安排，座位让他自己挑”这类仍在替人物展示价值观的精致句子。
- **时间格填满检查**：分镜表允许旁白留空、保留环境声，或者让一句话跨两个镜头，不再默认每格都要有完整观点。
- **结尾覆盖检查**：区分普通留白和结尾缺失；原稿末格有内容、改稿末格变空会被单独报出。
- **真实口播检查**：脱离标题和画面朗读，检查人物为什么此刻会说这句话，以及动词和宾语是否符合日常中文。
- **压缩金句检查**：识别“分两天，座位舒服，聊天从容”这类由多个短分句拼成的广告句。

自动报告只负责定位风险，不能单独证明“已经去干净”。最终仍需逐句通过口语、人物、画面分工和事实来源检查。

### 2026-07-19 补强：口吻差异必须落在台词里

新版增加三项硬检查：

- **元数据盲测**：人设名称、年龄、服装、画面和配音说明全部隐藏后，台词仍需保留可识别的注意力、句式、知识边界和情绪温度。
- **口吻分布检查**：不能让所有人物都使用“平静复述事件 + 完整解释动作 + 克制收尾”这一种安全口吻。每个主要人物组至少抽查五条实际口播。
- **整段重复检查**：报告完全重复的脚本和口播格，避免大批复制内容被不同编号或视觉设定掩盖。

调用示例：

```text
[$debug-aiwriting] 检查这批 UGC 人物口播：重点看不同人设是否仍在说同一种话、第一人称是否在替人物下结论、旁白是否复述画面、结尾是否强行升华或提问。保留原始事实，不要为了自然感补写未经提供的生活细节。
```

## 目录结构

```text
debug-aiwriting/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── scripts/
│   ├── audit_surfaces.py
│   ├── audit_ugc_scripts.py
│   └── test_audit_ugc_scripts.py
└── references/
    ├── ai-trace-checklist.md
    ├── client-proposal-playbook.md
    ├── correction-propagation.md
    ├── creative-ideation-filter.md
    ├── executive-report-register.md
    ├── external-facing-check.md
    ├── internal-ops-register.md
    ├── large-document-coverage.md
    ├── marketing-strategy-register.md
    ├── personal-voice-profile-example.md
    ├── plain-language-gate.md
    ├── reference-style-calibration.md
    ├── rewrite-playbook.md
    ├── ugc-persona-script-register.md
    └── whitepaper-case-register.md
```

## 安装

把仓库放到 Codex skills 目录下：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/zhongky1995/debug-aiwriting.git ~/.codex/skills/debug-aiwriting
```

之后在 Codex 中可以直接提到：

```text
[$debug-aiwriting] 帮我把这段话去 AI 味，并保留事实和口径
```

说明：`debug-aiwriting` 是 Codex 识别用的 skill 机器名；`Debug AI Writing` 是对外展示名。

## 自定义

开源版不默认附带任何人的个人口吻。需要长期使用自己的表达习惯时，新建 `local/personal-voice-profile.md`，结构可参考 `references/personal-voice-profile-example.md`。`local/` 已加入忽略列表，不会随普通提交上传。

修改多页 Markdown、XML、HTML 或长文本前，可以先生成文本表面清单：

```bash
python3 scripts/audit_surfaces.py <文件路径> --output <清单.json>
```

用户明确否定某个词或短语时，可通过 `--term` 将它作为本轮硬性排除项扫描。脚本只负责覆盖检查和风险提示，最终是否保留专业术语仍要结合场景判断。

检查表格型 DOCX 口播脚本库时，可以先生成确定性的风险报告：

```bash
python3 scripts/audit_ugc_scripts.py <脚本.docx> --output <报告.json>
```

如需检查改稿是否误删结尾，增加原稿作为基线：

```bash
python3 scripts/audit_ugc_scripts.py <改稿.docx> --baseline <原稿.docx> --output <报告.json>
```

报告会统计脚本数量、人设数量、配音说明覆盖率与集中度、整段重复脚本、重复口播格、第一人称结论公式、隐性价值总结、不自然动宾、压缩式金句、固定反问结尾、旁白格填满情况，以及原稿中非空结尾被改稿清空的数量和位置。它用于定位批量问题，不代替逐条理解人物和场景。

如果用于公司材料，建议重点维护：

- `references/external-facing-check.md`
- `references/client-proposal-playbook.md`
- `references/plain-language-gate.md`
- `references/large-document-coverage.md`
- `references/marketing-strategy-register.md`
- `references/reference-style-calibration.md`
- `references/ugc-persona-script-register.md`
- `references/whitepaper-case-register.md`
- `references/executive-report-register.md`
- `references/internal-ops-register.md`

## License

MIT
