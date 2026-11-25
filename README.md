# router-confesses

[![make.fun · u-carbon-forge-the-router-confesses-f98f6b9e](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)
[![rank](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/nmlyz/router-confesses/rank.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)
[![reward](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/nmlyz/router-confesses/reward.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-the-router-confesses-f98f6b9e)

router-confesses is a tiny program that writes one excuse line from a home Wi-Fi router to a file: the router saw the movie's twist coming three scenes early and, unable to watch the hero open that door, closed its own door instead. The line was picked from 53 candidates by pairwise judging against the brief — a router's own excuse, a twist in the last words, and a voice drawn from the router as a fellow viewer of the film.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 118 characters, a single line, and ends on its strongest beat. The program builds the line from two clauses — what the router saw coming, then the twist that turns the hero's door into the router's own — and checks the result against the entry gate (length, single line, no leading or trailing space, exact judged length and byte length) before writing it.

---

<sub>See the line on [make.fun](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)</sub>
