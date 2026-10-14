# 金字塔表达工作室 · Pyramid Studio

**把零散材料整理成先有结论、再有支持的表达。** 一个 Codex skill，统一写邮件、做汇报、搭报告、编 PPT 故事线、分析问题和检查逻辑。

技能名：`pyramid-studio`。无需 API Key，无需安装其他 skill；联网查证或实际生成 PPT 文件，仍依赖所在环境的相应工具。

## 30 秒开始

安装后在 Codex 新聊天输入：

```text
$pyramid-studio 把下面材料整理成给老板的周报，200字以内，只使用给定事实：
接口开发已完成；测试未完成；计划周五上线。
```

可得到这样的表达（模型实际措辞可能不同）：

> 接口开发已完成，测试仍未完成。周五上线是当前计划，尚不能确认能否按期。

它会保留“计划”的状态，不把它改成上线承诺。

## 安装到 Codex

下载本仓库 ZIP 并解压，在仓库目录运行（需要 Python 3）：

```sh
python3 scripts/install.py --dry-run
python3 scripts/install.py
```

默认复制到 `$CODEX_HOME/skills/pyramid-studio`；未设置 `CODEX_HOME` 时为 `~/.codex/skills/pyramid-studio`。如有不同内容的同名技能会停止，避免覆盖。相同版本重复运行会提示已安装。升级前先把旧目录备份到 skills 目录之外，再运行安装器。

也可以手动复制整个 `skills/pyramid-studio` 文件夹到 Codex 的 skills 目录。复制的是包含 `SKILL.md` 的整个目录，而不是只复制一个文件。新开 Codex 聊天以刷新技能发现；若仍未出现，重启 Codex。

## 怎么提问

最有用的四项输入：**读者、要回答的问题、原始材料、输出形式**。不必写专业术语，也不用每次填表。

| 场景 | 可直接复制的提示词 |
|---|---|
| 邮件/周报 | `$pyramid-studio 给老板写一封150字邮件，说明当前进展与待确认事项。仅使用以下事实：……` |
| 报告 | `$pyramid-studio 用这些材料搭一份预算申请报告的详细提纲，读者是财务负责人，缺证据的地方标出来：……` |
| PPT | `$pyramid-studio 帮我做一份10分钟项目汇报故事线，列每页观点标题、证据、图示建议和讲稿要点：……` |
| 问题分析 | `$pyramid-studio 分析转化率下降问题，先区分已知事实和原因假设，再列验证计划：……` |
| 审稿 | `$pyramid-studio 只检查下面文稿的结构与逻辑，不全文重写；按影响列问题和对应修改建议：……` |
| 学习 | `$pyramid-studio 用一个简短例子解释SCQA，再让我做一道练习。` |

也可用 Git 安装：

```sh
git clone https://github.com/jiazhaojune-gif/pyramid-principle-studio.git
cd pyramid-principle-studio
python3 scripts/install.py
```

## 它如何工作

1. 找到读者真正要回答的问题。
2. 提炼一个材料支持的中心回答；证据不足时先标出问题。
3. 把理由、步骤或证据按同一父问题分组并排序。
4. 按邮件、报告、演示或审稿任务交付结果。
5. 对照原材料检查数字、范围、语气与事实力度。

不会强凑三点，不强制所有开头套四段 SCQA，也不会因为要让报告完整就虚构收益或数据。纯结构审稿不等于事实核实。

## 两份资料怎样组合

采用 **一个统一入口 + 按需参考模块**：中文资料补充问题界定、诊断与学习模式；原六技能资料补充短文、长文、演示、审稿与来源核对。统一流程替代跨插件调用，全部参考资料在同一技能目录内可读。

```text
skills/pyramid-studio/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── workflows.md       # 短文、长文、演示
    ├── audit.md           # 结构诊断
    ├── analysis.md        # 问题界定与验证
    ├── evidence.md        # 来源与数据边界
    ├── learning-map.md    # 学习导航
    └── …                 # 章节、案例、术语等按需资料
```

## 分享介绍与海报

- [可转发介绍](docs/INTRODUCTION.md)
- [来源、改动与许可范围](docs/SOURCES.md)
- [使用示例与行为验收](docs/ACCEPTANCE.md)
- [一张看懂：苹果风使用海报](posters/pyramid-studio-guide.png)，集中介绍用途、输入方式、调用指令和示例。由内置 image_gen 生成，完整提示词见 [POSTER-PROMPTS.json](docs/POSTER-PROMPTS.json)。

![一张看懂金字塔表达工作室](posters/pyramid-studio-guide.png)

## 来源与许可

方法基于 Barbara Minto 的金字塔原理。本项目包含用户提供并确认可公开再分发的两份资料，保留上游作者信息及 Apache-2.0 来源部分的许可证。**公开仓库不等于整套内容均以 Apache-2.0 开源**；完整范围见 [SOURCES.md](docs/SOURCES.md) 与 [NOTICE](NOTICE)。项目与原书作者、上游作者或 Johnson & Johnson 无官方关联。
