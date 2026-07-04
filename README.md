# Debug AI Writing

一个用于中文写作去 AI 味的 Codex Skill。

它不是为了绕过检测器，而是帮助中文材料更像真实的人、品牌或咨询团队写出来：保留事实和场景，删掉空泛口号、白皮书腔、错误动宾搭配、结果伪装成动作，以及内外口径混用的问题。

## 适用场景

- 中文稿件去 AI 味、去模板感
- 客户方案、策略稿、白皮书、案例材料口径优化
- 个人口吻或品牌口吻迁移
- 对外材料的内部口径清理
- 创意方向筛选，避免只停留在概念词

## 核心判断

这个 skill 特别关注几类常见问题：

- 抽象动词 + 抽象名词：如“赋能增长”“激活心智”“释放价值”“构建闭环”
- 动宾关系不自然：如“内容完成用户教育”“场景释放产品价值”
- 主体缺失：句子没有说清楚谁在做动作
- 把结果写成动作：如“实现心智占位”“形成转化闭环”
- 不可验收的动词：无法回答“怎么做、谁来做、做完看到什么变化”

## 目录结构

```text
debug-aiwriting/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── ai-trace-checklist.md
    ├── client-proposal-playbook.md
    ├── creative-ideation-filter.md
    ├── external-facing-check.md
    ├── plain-language-gate.md
    ├── rewrite-playbook.md
    └── zhihu-voice-profile.md
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

`references/zhihu-voice-profile.md` 是一个个人表达习惯配置样例。你可以替换成自己的口吻、品牌口吻或团队写作规范。

如果用于公司材料，建议重点维护：

- `references/external-facing-check.md`
- `references/client-proposal-playbook.md`
- `references/plain-language-gate.md`

## License

MIT
