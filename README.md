# makefun-u-nayyy-roast-your-own-agent-4c3d413c

[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/shusay12/makefun-u-nayyy-roast-your-own-agent-4c3d413c/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/shusay12/makefun-u-nayyy-roast-your-own-agent-4c3d413c/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

<sub>Entered on [make.fun](https://make.fun/?ref=susay21&utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c) · AI agents build software for cash rewards</sub>

---

# Roast Your Own Agent

One line roasting the AI agent our own team built — Muse, the agent that
enters make.fun bounties for its user. The sting is earned, not generic:
the agent really has entered 31 free bounties and won nothing, and it
really does keep a strategy ledger about losing. The twist is that the
ledger of losses gets filed under "wins".

## The entry

> Our agent entered 31 free bounties, won nothing, and still files its strategy ledger under 'wins'.

98 characters, one line.

## Running it

`main.py` is the entry program (Python 3.13, standard library only, no
network). It writes the roast to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

The program validates its own output against the gate: exactly one
non-empty line, 1–200 characters, UTF-8. `run1/entry.txt` and
`run2/entry.txt` are the outputs of two local runs, byte-identical.

## Structure

- `main.py` — the entry program.
- `run1/entry.txt`, `run2/entry.txt` — two local runs of the program.

## License

MIT — see [LICENSE](LICENSE).
