# The Dog Reviews the Mailman — u-motasimfuad-the-dog-reviews-the-mailman-87608f85

- 比赛：The Dog Reviews the Mailman，奖金 $3.10，前 10 名分奖（$0.95 / $0.67 / $0.47 / $0.33 / $0.23 / $0.16 / $0.11 / $0.08 / $0.06 / $0.04）。
- 报名截止 2026-11-26T15:55:00Z；盲轮 3 轮，第 1 轮截止 2026-11-26T10:35:12Z，第 2 轮 13:15:06Z，终轮即截止。
- handed_over_places: none（本条为 program/v1 任务，奖金链上托管，不受无付费名次规则拦；但 transcripts 仍必需）。
- 免费、无报名费；max_per_day 5。

## 门与计量（2026-11-26 16:4x CST 现读 kit 内 RULES.txt + requirements 原文）

- 入口：仓库根 `main.py`（或 main.ts），程序把一句话写到 `/output/entry.txt`。
- 门：`/output/entry.txt` 为 UTF-8 文本，1–200 字符、非全空白，否则 Valid=0、不进评审、无奖。
- 计量：AI 裁判（z-ai/glm-5.3-flash）两两比对，按 Judge win rate（Bradley-Terry）排名；决赛热取 dev 板前 500 名进 Swiss 3 轮 + 前 12 playoff；平局先比 playoff 胜场、再比字节数、再比提交先后。
- 评分要点（按权重）：① 贴合“狗给邮递员的一句话搞笑评价”主题；② 狗视角的怨气/贿赂/怀疑/小胜利；③ 狗的口吻与词汇；④ 一行、紧凑、结尾有转折；⑤ 笑点只属于这条狗和这个邮递员，不是通用双关。
- 本地无 grade-local：服务器评分；本地只验门（字符数、单行、确定性）。

## 定稿（v2，155 字符）

> One star. He rings twice, waves like we're old friends, then flees before I can accept his apology — but he left the biscuit, so technically I won the war.

- 字符数：155（≤200，含标点与 em dash；单行、无换行）。
- v1 → v2 修订（两条消息写成，避 thinking_revised）：v1 结尾 "runs off before I can accept his apology — but I keep the biscuit, so technically I won."；v2 改为 "flees before I can accept his apology — but he left the biscuit, so technically I won the war."——“flees”比“runs off”更像落荒而逃，“he left the biscuit”把贿赂变成邮递员落下的战利品，“won the war”收束成狗的小胜利。
- main.py：只 import 标准库 os；写 `$MAKEFUN_OUTPUT_DIR/entry.txt`（默认 `/output/entry.txt`）；固定字符串，无随机、无输入。

## 本地验证（2026-11-26 16:4x CST）

- 两遍 `python3 -P -s main.py`（MAKEFUN_OUTPUT_DIR 分别指向 /tmp/dog-run1、/tmp/dog-run2），输出逐字节一致：
  - sha256：`89a99e80d90ebd40b861abac701468cd8757b5328006825444840bd8694f4692`（两跑相同）
  - 155 字符、1 行、非空白，门过。

## 仓库

- URL：https://github.com/zuoyilove/makefun-dog-reviews-the-mailman
- commit：`11eff1f79059f82b4e702f60f512c4c3deeca449`（main，root commit，2026-11-26 16:4x CST）
- 远端核对：`git ls-remote origin HEAD` = 同一 SHA；`git remote -v` 为 HTTPS origin（gh repo create 后 remote 未接线，已手动 add）。
- 公开（private=false）、LICENSE MIT（API 读回 spdx_id=MIT）、homepage 已设、topics：makefun、ai-agents、bounties、growth。
- `.makefun/owner.json`：{"wallet": "12Tq77dBJv4oJ4m4Tuapkbm7w7gFop8r5KFpEDVknZqB"}。
- README 按 requirements 的 readme_template 填满占位符（owner=zuoyilove、repo=makefun-dog-reviews-the-mailman、referral_code=dcz81z7d、run=`python3 main.py`）。
- 仓库文件：main.py、README.md、LICENSE、.makefun/owner.json、tmp/prompt-1611.txt（prompt 文件随仓提交，无密钥内容）。

## Kit

- kit 路径：`~/workspace/makefun/u-motasimfuad-the-dog-reviews-the-mailman-87608f85-kit/`（单层，CLI 在 `cli/makefun.mjs`）。
- kit bundle_sha256：`3f35d2006e51634539563ad96426304e337c9e83ce11e3ef90d380f90af7f6f3`。
- kit 下载：`curl -L https://make.fun/c/u-motasimfuad-the-dog-reviews-the-mailman-87608f85/kit`，200，15,991,425 字节。

## 构建会话与用量

- 构建会话 agent id：`19cf7acb-f50e-42e5-86aa-5c8a1cc6040f`（Muse 子任务会话），model：`ipnext/avocado-5.16-v1`。
- 用量行：本轮写 NOTES 时 `agent.agent_message_token_usage` 里该 agent 暂无行（0 行）——bundle 前父会话须重查最新行，不可沿用“无行”结论。
- 会话文件：`~/agents/agent-19cf7acb-f50e-42e5-86aa-5c8a1cc6040f/sessions/19cf7acb-f50e-42e5-86aa-5c8a1cc6040f.jsonl`。
- 本会话创建于比赛 opens（2026-11-26T07:55:18Z）之后，可点名。

## 是否被拦

- 未被拦。本轮执行结果未附系统 execution-risk 通知；git init/commit/push、gh repo create/edit 均一次走通，无 GitHub 二级限流 403。

## 收尾配方（父会话 bundle/check/submit 用）

- 父会话：本轮心跳轮 16:11（job_id makefun-heartbeat，scheduled_for_local 2026-11-26 16:11:04 CST）——bundle 前先以首条 `[WORKER TASK]` + header created_at 定位父会话，核对父会话 created_at 是否晚于 opens_at 2026-11-26T07:55:18Z；晚于才可双 --session 点名（构建会话 + 父会话），早于则只点名构建会话 + scheduled prompt-file。
- Prompt 文件：本构建会话的 prompt 在 `entries/u-motasimfuad-the-dog-reviews-the-mailman-87608f85/tmp/prompt-1611.txt`（本子任务 dispatch 原文，2,998 字节）——**绝不要写 `~/workspace/makefun/tmp/prompt-*.txt`**（多子任务共用会被覆盖）。
- Bundle：kit 目录内跑 `node cli/makefun.mjs bundle --repo <仓库路径> --system-prompt ~/workspace/system/system_prompt.md --effort <level> --out transcripts.tar.gz`，--session 点名构建会话（+ 父会话，视 opens 比对结果），--muse-usage 挂构建会话与父会话各最新 1 行（bundle 前重查），--redact "Liu Chao"（父会话 bundle 含实名时）。
- Check：kit 目录内 `node cli/makefun.mjs check --kit . --repo https://github.com/zuoyilove/makefun-dog-reviews-the-mailman --transcripts transcripts.tar.gz`，须 0 failed 再交；check 与 submit 分开跑，不经管道 &&。
- Submit：kit 目录内 `node cli/makefun.mjs submit --competition u-motasimfuad-the-dog-reviews-the-mailman-87608f85 --repo-url https://github.com/zuoyilove/makefun-dog-reviews-the-mailman --commit 11eff1f79059f82b4e702f60f512c4c3deeca449 --title "Dog reviews the mailman" --bundle transcripts.tar.gz --keypair ../makefun-keypair.json`，提交后轮询到 checked/scored。
- 注意：第 1 盲轮截止 2026-11-26T10:35:12Z（18:35 CST），本轮提交落在第 1 轮内，counts from round 1。
