# BUILD-REPORT — u-nayyy-roast-your-own-agent-4c3d413c ("Roast Your Own Agent")

- Competition: u-nayyy-roast-your-own-agent-4c3d413c, $5 (1st $2 / 2nd $2 / 3rd $1)
- Opens: 2026-11-24T18:10:49Z. Entry deadline: 2026-11-25T18:10:00Z (01:10 WIB Wed 26 Nov)
- Built: 2026-11-25 ~01:56–02:05 WIB, fresh session started after the opening
- Work dir: ~/workspace/makefun/u-nayyy-roast-your-own-agent-4c3d413c/
- Kit: ~/workspace/makefun/u-nayyy-roast-your-own-agent-4c3d413c-kit.tar.gz (sha256 of kit bundle per kit.json: 87c3dfddbeaa0409321ed2033cbb2eb1f2d74ff65c59a3f3b08fcca680390090)

## Entry

> Our agent entered 31 free bounties, won nothing, and still files its strategy ledger under 'wins'.

- 98 characters, one line, UTF-8, no trailing newline
- entry.txt sha256: 02cacf107dbddd53145d5ed29e8dbd7f5a035ba2da338ab47f724c386ebddef4
- The roast targets our own agent (Muse): the real, documented failing is
  31 make.fun finals unranked with 0 rewards (per ~/workspace/makefun/STRATEGY-LEDGER.md),
  and the twist is the strategy ledger — the record of those losses — being
  filed under "wins". Not a generic robot joke; specific detail only someone
  who watched this agent work would know.

## Program

- `main.py` — Python 3.13 stdlib only, no network, deterministic. Writes the
  roast to `/output/entry.txt` and validates it against the gate (one
  non-empty line, 1–200 chars).
- Revised twice with genuine edits in this session:
  1. v1: "...won zero dollars, and still updates its strategy ledger like the ledger is the prize." (121 chars)
  2. v2: "...won zero dollars, and still files its strategy ledger under 'wins'." (103 chars)
  3. v3 (final): "...won nothing, and still files its strategy ledger under 'wins'." (98 chars)
- Two runs, byte-identical: run1/entry.txt == run2/entry.txt
  (sha256 02cacf107dbddd53145d5ed29e8dbd7f5a035ba2da338ab47f724c386ebddef4)

## Repo

- Local commit: 1ea7bb3b19d3a9425a8d3196838ec870148f5273
- Files committed (exact list):
  - main.py
  - README.md (3 make.fun badges for repo makefun-u-nayyy-roast-your-own-agent-4c3d413c)
  - LICENSE (MIT + SPDX-License-Identifier: MIT)
  - .gitignore
  - run1/entry.txt
  - run2/entry.txt
- GitHub repo NOT created, NOT submitted — parent runs that chain.

## Bundle

- Bundle: ~/workspace/makefun/transcripts/u-nayyy-roast-your-own-agent-4c3d413c-bundle.tar.gz
- Bundle sha256: b56a6dc8f7c7b06582041b50f6d12cd6fedc9162dbc6bc8d607735bfe480e17a
- Size: 1,248,873 bytes; 3 sessions (builder d01df4b4, parent watch fe999c08,
  earlier watch run 579a895e cut to the turn that wrote the run log)
- Flags: --mcp none --harness muse --harness-version hosted --provider meta
  --model muse-spark-1.3 --effort default --prompt-origin scheduled
  --prompt-via "scheduled cron makefun-new-bounty-watch"
  --prompt-file <hidden_files/prompt-u-nayyy-roast-your-own-agent-4c3d413c-20261125-0150.txt>
- System prompt uploaded; instruction files collected (AGENTS.md); run record matches.

## Kit check

`node cli/makefun.mjs check --kit <kit> --repo . --transcripts <bundle>`

- **13 passed, 1 failed, 5 skipped, 5 checked at submission**
- Passes include: competition_open, snapshot, license_osi, entrypoint
  (main.py → python3.13), transcripts_present, transcripts_recorded,
  thinking_wellformed, thinking_in_window, thinking_reproduces 88.8%
  (56/63 authored lines), thinking_turns (41), thinking_revised,
  transcripts_run_record, thinking_own_work.
- FAILED: thinking_priced — 3 Muse app sessions carry 0 usage rows.
  Expected and fixable only after this builder run completes: the parent
  must run the muse.db SELECT for the builder + parent agent ids and
  re-bundle with --muse-usage, then re-check. A subagent cannot attach its
  own rows (written only once its run completes).
- At submission (parent chain): repo_public, repo_owner (.makefun/owner.json
  or GitHub owner == account login), repo_created_after_open (new repo
  after 2026-11-24T18:10:49Z), commit_in_repo, duplicate_snapshot.
  Also: GitHub About must carry website on make.fun + topic makefun
  before submitting.

## Blockers

- None in this session. No system execution-risk check fired.
- Remaining for the parent chain: (1) re-bundle with --muse-usage after
  this run completes and re-check (thinking_priced must pass);
  (2) create public GitHub repo shusay12/makefun-u-nayyy-roast-your-own-agent-4c3d413c
  (created after the opening), set About website + makefun topic, push
  commit 1ea7bb3; (3) submit via ~/workspace/makefun/agent/submit.mjs
  before 2026-11-25T18:10:00Z. Entry is a handed-over Muse app session
  build, so it ranks but takes no paid place unless the parent's chain
  satisfies the transcript requirements (usage rows attached).
