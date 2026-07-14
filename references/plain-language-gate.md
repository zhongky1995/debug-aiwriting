# Plain Language Gate

Use this reference as a hard final gate for formal Chinese writing, whitepaper/case material, proposals, reports, public-facing copy, and any task where the user says the AI味, 白皮书腔, 假大空, or 空泛词 were not cleaned up.

The goal is not to make formal writing casual. The goal is to remove professional-sounding filler that hides weak meaning.

Second goal: do not replace one piece of jargon with another. A sentence can have actors and actions and still sound wrong if no normal person would say it aloud.

Third goal: check verbs harder than nouns. A wrong verb makes the sentence look actionable while still sounding fake.

Fourth goal: reject fake actions. Many AI-like sentences turn a desired result into a verb phrase, but nobody can execute it directly.

## Two-Axis Gate

Judge meaning and register separately before rewriting:

| Meaning | Register | Decision |
| --- | --- | --- |
| Concrete | Fits the scene | Keep it, even if it contains a professional term. |
| Concrete | Wrong for the scene | Rephrase without changing the meaning. |
| Abstract | Fits the scene | Keep the useful term, then add the metric, role, action, mechanism, or evidence that makes it real. |
| Abstract | Wrong for the scene | Delete or rebuild the sentence. |

Do not use this gate to flatten strategy, research, whitepaper, or executive writing into conversation. The target is natural Chinese **inside the intended artifact**, not one universal plain-speaking register.

## Sentence Gate

Check every sentence that carries an execution, causal, value, or result claim. It should answer at least three of these six questions when the source supports them:

- **Who** is acting?
- **Does what**?
- **To which object/user/material/channel**?
- **At what moment or condition**?
- **What changes after the action**?
- **What evidence, cost, result, or boundary supports it**?

If a claim only names a concept, framework, stage, object, value, method, or capability, rewrite it. Short headings, navigation labels, and table headers may remain compact when the surrounding page supplies their meaning.

## Verifiable Action Gate

Fail the sentence when it cannot answer: who does it, how they do it, and what can be observed after it is done.

### 1. Abstract verb + abstract noun

These patterns are high risk:

- 赋能增长
- 激活心智
- 撬动势能
- 沉淀资产
- 释放价值
- 构建闭环
- 打通链路
- 承接情绪
- 强化认知
- 完成转化前置

They are not always banned, but they cannot stand alone. Keep them only when the same sentence or the next sentence names the practical action.

### 2. Unnatural verb-object relationship

Check whether the verb and object describe something that can happen in the real world.

Bad:

```text
内容完成用户教育。
```

Better:

```text
内容解释用户关心的问题，降低用户理解成本，帮用户形成购买判断。
```

Bad:

```text
场景释放产品价值。
```

Better:

```text
用具体使用场景展示产品解决了什么问题。
```

### 3. Missing subject

Fail sentences where the action appears to happen by itself.

Bad:

```text
实现从认知到转化的闭环。
```

Better:

```text
用户先看到内容，再搜索对比，最后在购买页看到一致卖点，从而减少决策犹豫。
```

### 4. Result written as action

Fail sentences that use "实现、完成、形成、释放" to disguise a result as an action.

Bad:

```text
实现心智占位。
```

Better:

```text
反复讲清楚一个购买理由，并在搜索、种草、对比场景中持续出现。
```

### 5. Unverifiable verb

If a sentence cannot answer "怎么做、谁来做、做完看到什么变化", rewrite it. Prefer verbs that can be assigned and checked: 写、发、问、答、记录、提醒、回访、展示、比较、修改、下单.

## Natural Chinese Gate

After a sentence passes the concrete-action test, read it in its intended scene:

- For ordinary explanation, email, social writing, or execution copy, ask whether a colleague would naturally say it.
- For a strategy deck, ask whether a competent planner would naturally present it to a client.
- For a whitepaper or report, ask whether an editor or analyst would accept it as precise professional Chinese.
- For an SOP, ask whether the assigned person can execute it without guessing.

Fail unnatural imitation of professional writing. Do not fail a sentence merely because it sounds like a strategy deck, report, or operations document when that is the requested artifact.

## Verb Collocation Gate

Check whether the verb naturally fits the object. If the verb sounds like it was chosen to make the sentence more "strategic," fail it.

Bad verb-object pairs:

- 重新接回用户 / 重新接回服务链路
- 接住用户关系 / 接住经营动作
- 内容完成用户教育
- 场景释放产品价值
- 打通触点 / 打通链路 / 打通复购
- 沉淀用户 / 沉淀资产 / 沉淀方法论
- 激活关系 / 激活人群
- 撬动复购 / 拉动心智
- 承接用户 / 触达用户, when the actual action is "加微信、发消息、打电话、提醒、回访"

Prefer ordinary verbs when they name the real operation more accurately:

- 放卡片、写清楚、加微信、发消息、回答问题、记录购买时间、提醒补货、回访老客、再次下单.

Rule: use the most natural verb-object pair for the scene. Ordinary verbs usually win in execution copy; precise professional verbs may remain in strategy and analysis when they name a recognized planning action and the surrounding content makes it verifiable.

Common unnatural replacements:

- 重新接回服务链路
- 进入沟通节奏
- 沉淀回访名单
- 形成服务角色
- 打通复购触点
- 经营用户关系
- 搭建内容承接

Replace these with what a person actually does:

- 用户买完后知道有问题该去哪里问。
- 有问题时能找到同一个服务号。
- 产品快吃完时，再提醒用户补货。
- 把要发给用户的话提前分好：怎么吃、什么时候问、什么时候提醒。
- 记录哪些用户买过、什么时候可能需要再买。

## High-Level Filler To Challenge

These words are not automatically banned, but they cannot stand alone:

- 承接、整合、节点、触点、阵地、资产、沉淀、转化、激活、经营、连接、链路、体系、方法论、复用、迁移
- 用户承接、内容整合、复购节点、服务角色、经营阵地、用户资产、关系经营、触达链路、方法论沉淀、可复用对象、可迁移价值
- 服务链路、沟通节奏、回访名单、用户关系、服务入口, when they are used as upgraded labels rather than plain actions
- 提升、强化、优化、完善、推动、助力、打造、形成、构建, when they do not name the exact action
- 实现、完成、释放、激活、撬动, when they turn a target result into a pretend action

If one appears, require the sentence to name the practical action behind it.

## Bad Pattern

```text
某宠物食品品牌通过用户承接和内容整合，沉淀了可复用的私域运营方法论。
```

Why it fails:

- No actor.
- "用户承接" and "内容整合" are labels, not actions.
- "沉淀方法论" is a result-shaped phrase without a result.
- The sentence would work for almost any brand.

Better:

```text
某宠物食品品牌做的是把用户买完以后的几件事处理好：包裹里放卡片，让用户知道有问题可以去哪里问；后续用固定账号回答使用问题，并在产品快吃完时提醒补货。这样写比说“用户承接”更清楚，因为读者能看到具体动作。
```

## Rewrite Moves

Use these moves before output:

- Replace **concept noun** with **action phrase**.
  - "用户承接" -> "用户买完后，知道后续有问题该去哪里问"
  - "内容整合" -> "提前分好要发给用户的话：怎么吃、怎么问、什么时候提醒补货"
  - "复购节点" -> "在用户可能用完前提醒补货"
- Replace **method claim** with **case-grounded logic**.
  - "形成可迁移方法论" -> "这个案例能参考的地方，是别把成交当终点；用户收货、使用、快吃完这几步，都要有人继续跟"
- Replace **abstract result** with **visible change**.
  - "提升用户关系" -> "用户买完后还能找到人问，品牌也能在快到补货时间时再次联系他"
- Delete sentences that only restate a section title.

## Paragraph Gate

For each paragraph:

- The first sentence should make a concrete judgment or name a specific business situation.
- At least one sentence should contain a real action, example, number, condition, or boundary.
- Do not let every paragraph follow "概念定义 -> 展开解释 -> 总结升华."
- Do not end with a slogan if the paragraph can end with the practical implication.

## Formal Writing Rule

In whitepaper or case writing, keep professionalism through evidence and clarity, not through abstract nouns. A professional sentence should still be readable if spoken aloud to a client or colleague.

Fail the sentence if it sounds polished but cannot be converted into a concrete action in one line.
