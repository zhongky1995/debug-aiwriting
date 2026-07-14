# Debug AI Writing

一个用于中文写作去 AI 味的 Codex Skill。

它不是为了绕过检测器，而是帮助中文材料更像真实的人、品牌或咨询团队写出来：保留事实和场景，删掉空泛口号、白皮书腔、错误动宾搭配、结果伪装成动作，以及内外口径混用的问题。

## 适用场景

- 中文稿件去 AI 味、去模板感
- 客户方案、策略稿、白皮书、案例材料口径优化
- 个人口吻或品牌口吻迁移
- 对外材料的内部口径清理
- 创意方向筛选，避免只停留在概念词
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

## 目录结构

```text
debug-aiwriting/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── scripts/
│   └── audit_surfaces.py
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

如果用于公司材料，建议重点维护：

- `references/external-facing-check.md`
- `references/client-proposal-playbook.md`
- `references/plain-language-gate.md`
- `references/large-document-coverage.md`
- `references/marketing-strategy-register.md`
- `references/reference-style-calibration.md`
- `references/whitepaper-case-register.md`
- `references/executive-report-register.md`
- `references/internal-ops-register.md`

## License

MIT
