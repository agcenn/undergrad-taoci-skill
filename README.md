# undergrad-taoci-skill

> 面向本科生的导师科研套磁 Skill：不是帮你群发 100 封信，而是帮你找到真实的匹配点，把一封信写对。

[English](README_EN.md)

## 这是什么？

`undergrad-taoci` 是一个面向本科生的 Agent Skill，核心任务是：

**分析“本科生背景 × 导师近期研究”，找到最可信的套磁切入点，并生成真实、具体、简短、可直接发送的导师套磁信。**

它尤其适合这些情况：

- 没有论文，只有课程项目 / GitHub / 竞赛 / 自学经历；
- 已经有目标导师，但不知道邮件里到底该写什么；
- 想找导师，却不知道谁更适合本科生联系；
- 邮件写得像模板、像个人陈述，或者“AI 味”很重；
- 担心为了显得厉害而夸大经历；
- 导师没回复，或已经回复但不知道下一步怎么处理。

## 安装：30 秒上手

> 推荐普通用户优先使用 **方法 1**。不需要手动找 skills 目录，也不需要先学 Git。

### 方法 1：使用 `$skill-installer`（推荐）

在 Codex 中输入：

```text
$skill-installer
```

然后告诉它：

```text
Install the skill from:
https://github.com/agcenn/undergrad-taoci-skill
```

安装完成后，如果 Skill 没有立即出现，重新打开 Codex。

然后直接使用：

```text
$undergrad-taoci 帮我根据我的简历和目标导师主页写一封本科生科研套磁信。
```

也可以不显式调用 Skill，直接描述任务：

```text
我是计算机本科生，这是我的简历和目标导师主页。
请分析我和导师的匹配点，并帮我写一封真实、简短、有针对性的套磁信。
```

### 方法 2：Git Clone（适合开发者）

Codex 用户级 Skill 默认可放在 `$HOME/.agents/skills`。

macOS / Linux：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/agcenn/undergrad-taoci-skill.git ~/.agents/skills/undergrad-taoci
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
git clone https://github.com/agcenn/undergrad-taoci-skill.git "$HOME\.agents\skills\undergrad-taoci"
```

重新打开 Codex 后输入：

```text
$undergrad-taoci 帮我写一封本科生科研套磁信。
```

### 方法 3：手动复制（已下载 ZIP）

如果你已经从 GitHub 下载并解压了本项目，只需要把整个项目文件夹复制到用户级 skills 目录。

macOS / Linux：

```bash
mkdir -p ~/.agents/skills
cp -R undergrad-taoci-skill ~/.agents/skills/undergrad-taoci
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse undergrad-taoci-skill "$HOME\.agents\skills\undergrad-taoci"
```

复制完成后重新打开 Codex。

### 检查是否安装成功

在 Codex CLI / IDE 中可以输入：

```text
/skills
```

或者直接输入 `$`，查看是否能看到：

```text
undergrad-taoci
```

看到后即可使用。

### 项目级安装（可选）

如果你只想让当前项目使用这个 Skill：

```bash
mkdir -p .agents/skills
git clone https://github.com/agcenn/undergrad-taoci-skill.git .agents/skills/undergrad-taoci
```

### 其他 Agent

本仓库遵循 Agent Skills 的 `SKILL.md` 目录结构。对于支持 Agent Skills 的其他客户端，请将整个 `undergrad-taoci` 目录放入对应 skills 目录，并保留 `SKILL.md`、`references/`、`agents/` 等相对路径。

## 核心边界

这个 Skill 的主任务不是“从零教你做科研”，而是 **完成高质量本科生套磁**。

主流程：

```text
学生背景
   ↓
导师研究核验
   ↓
匹配点 / Research Readiness
   ↓
套磁策略
   ↓
套磁信
   ↓
质量检查与自动修订
   ↓
最终可发送版本
```

完成套磁信后，才会提供一个可选入口：如果用户已经进入导师考核或进组阶段，可以继续分析任务、入门路线和第一次汇报；用户没有明确需要时不会主动展开。

## v0.2.0 有什么变化？

相比 v0.1.0：

- 把核心重新收敛到 **本科生套磁信**；
- 将超长 `SKILL.md` 拆成“路由 + references”，减少无关上下文；
- 增加 5 个工作模式：导师搜索、导师分析、写信、审信、跟进/回复；
- 增加 **Research Readiness Gap**，明确“可以写什么 / 不能夸大什么”；
- 增加 `agents/openai.yaml`；
- 增加行为 eval、隐私扫描、结构校验和 GitHub Actions；
- 增加可选的套磁进度 ledger；
- 更新 Codex 安装方式，使用当前 `.agents/skills` 路径。

完整变化见 [CHANGELOG.md](CHANGELOG.md)。

## 能做什么？

| 场景 | 输出 |
|---|---|
| 不知道联系谁 | 筛选 3–5 位更值得深入看的导师 |
| 已有目标导师 | 近期研究速览、匹配点、本科生参与证据、不确定项 |
| 要写套磁信 | 套磁切入点 + 中文/英文最终邮件 |
| 已有一封邮件 | 群发感 / 夸大 / 空泛 / 篇幅 / AI 味检查 + 完整修订版 |
| 背景不完全匹配 | Research Readiness：能写什么、哪些不能装懂、是否需要小准备 |
| 导师没回复 | 一次简短、低打扰 follow-up |
| 导师已回复 | 判断回复类型并处理下一步 |

## 最核心的三条规则

1. **不编造**：没有论文就不写论文；没有排名就不猜排名；没有读过论文就不写“拜读”。
2. **不群发**：每封信至少有一个真实、可解释的导师专属研究锚点。
3. **本科生视角**：课程项目、GitHub、竞赛、工程实现和学习能力都可以成为可信证据。

## 快速使用

### 直接写信

```text
使用 $undergrad-taoci。
我是西安交通大学计算机本科生，这是我的简历和目标导师主页。
请先找出我和导师真正匹配的地方，再帮我写一封中文套磁信。
不要夸大我的经历。
```

### 只有导师主页，没有明确切入点

```text
使用 $undergrad-taoci 分析这个导师：<URL>
我会 C/C++、Python，做过系统课程和一个 Ascend C 项目。
请告诉我最适合从什么角度套磁，然后直接给最终邮件。
```

### 不知道找谁

```text
我是计算机本科生，想找浙江大学做 AI Systems / LLM Systems 的导师。
我会 C/C++、Python，有系统课程和 GitHub 项目，但没有论文。
使用 $undergrad-taoci 帮我筛 5 位，然后告诉我最应该先联系谁。
```

### 检查已有邮件

```text
使用 $undergrad-taoci 检查这封套磁信。
重点看：群发感、夸大、AI 味、是否太长，并给我完整修改版。
```

## 工作模式

```text
A. Mentor Search
   不知道找谁 → 筛导师

B. Mentor Analysis
   已有导师 → 近期研究 + 匹配分析

C. Outreach Draft  ← 核心
   背景 × 导师 → 套磁切入点 → 最终邮件

D. Outreach Review
   已有邮件 → 查硬伤 → 完整修订版

E. Follow-up / Reply
   已发送 → 跟进或处理导师回复
```

## 导师匹配评分

只有需要比较多位导师时才使用：

```text
研究方向匹配       40%
学生经历匹配       25%
本科生参与证据     20%
近年研究持续性     15%
```

注意：**这个分数不是录取概率，也不是回复概率。**

若“本科生参与证据”没有公开信息，Skill 应标记为未知，而不是硬给一个高分。

## Research Readiness

本科生最常见的问题不是“完全不匹配”，而是：有基础，但不知道哪些能写、哪些不能夸大。

例如：

```text
导师方向：LLM inference / AI Systems

你的背景：
✓ C/C++
✓ Computer Systems
✓ Ascend C kernel
△ PyTorch
✗ vLLM
✗ LLM inference project

邮件可以强调：
- systems / kernel 基础
- 低层优化经验
- 对 inference efficiency 的明确兴趣

邮件不能写：
- “我有丰富的 LLM inference 经验”
```

Research Readiness 只服务于套磁，不会默认展开成数月科研路线。

## 邮件质量标准

最终邮件至少应该满足：

- 学生事实真实；
- 至少一个导师专属研究锚点；
- “我的经历”和“导师研究”之间有明确连接；
- 请求清楚；
- 本科生语气，不装专家；
- 30 秒左右能看完；
- 把导师名字删掉后，不能原样群发给十位老师。

## 项目结构

```text
undergrad-taoci-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── mentor-search.md
│   ├── mentor-analysis.md
│   ├── research-readiness.md
│   ├── outreach-strategy.md
│   ├── email-writing.md
│   ├── email-review.md
│   ├── integrity.md
│   ├── follow-up.md
│   └── reply-handling.md
├── examples/
├── evals/
├── templates/
│   └── outreach-ledger.csv
├── scripts/
├── .github/workflows/validate.yml
├── VERSION
└── CHANGELOG.md
```

## 测试

运行所有确定性检查：

```bash
python scripts/run_checks.py
```

单独查看行为 eval：

```bash
python scripts/run_evals.py --list
python scripts/run_evals.py --case hallucination-paper
```

`evals/cases.json` 描述的是 **Agent 行为测试**。CI 会验证测试定义与仓库结构，但不会假装在没有模型运行的情况下评估真实生成质量。行为质量需要把测试 prompt 交给支持该 Skill 的 Agent 执行并按 `must` / `must_not` 判定。

## 可选套磁记录

同时联系多位导师时，可以复制：

```text
templates/outreach-ledger.csv
```

记录 `researched / drafted / contacted / waiting / replied / joined` 等状态。单导师套磁不强制使用。

## 隐私与学术诚信

不要提交身份证号、账号密码、API Key 等无关敏感信息。

Skill 不应帮助用户虚构：

- GPA / 排名
- 奖项
- 论文
- 科研经历
- 项目结果
- 实习
- 导师招生状态
- 自己并未读过的论文经历

## 灵感来源

项目设计参考了社区中已有的套磁 / 保研 Skill 工程化思路，并重新面向本科生场景设计：

- [Kisechan/taoci-skill](https://github.com/Kisechan/taoci-skill)
- [syiibfs-hash/baoyan-skills](https://github.com/syiibfs-hash/baoyan-skills)

本项目的本科生定位、工作流、规则、references 和测试均独立编写。

## License

MIT License. See [LICENSE](LICENSE).
