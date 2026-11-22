# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/CharmLynn/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/CharmLynn/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One 1024×1024 newspaper front page summing up the world news of
21 November 2026: a lead story up top, four more in a grid below,
and the sources in the footer. Everything on it was drawn by code.

## The five stories

**COP31 talks run into overtime in Antalya** — the lead.
Negotiators miss the Friday deadline, deadlocked over a draft deal
with no mention of fossil fuels; a third text is due on Saturday.
(Hürriyet Daily News; Al Jazeera; Reuters.)

**Mexico captures "El Chapo Isidro".**
Special forces seize FBI most-wanted Fausto Isidro Meza Flores in
Guasave; four soldiers and seven gunmen are killed in the raid.
(Reuters; AP; NPR.)

**Russian strike hits Zelensky's home city.**
Ballistic missiles hit Kryvyi Rih on Friday night; a boy of 7 and
a woman of 20 are killed and 60 people are wounded. (AP; Al Jazeera.)

**Drones set Russian cargo ship ablaze.**
The Sparta II, bound for Kaliningrad, is hit in the Gulf of Finland;
its crew of 16 is evacuated as it drifts into Finnish waters.
(Reuters; Al Jazeera; CNN.)

**Mosquitoes cut dengue by 69% in Brazil trial.**
Wolbachia-carrying mosquitoes cut dengue and chikungunya in
schoolchildren in Belo Horizonte, researchers report. (AP; The
Straits Times.)

Each story happened, or was first reported, on 21 November 2026.

## Files

- `draw.py` — draws `entry.png` with Pillow: paper background,
  serif headlines, flat glyphs, all lettering rendered by code.
  Run it twice and the file comes out byte-identical.
- `entry.png` — the finished front page, 1024×1024 pixels.
- `main.py` — the entry program (Python 3.13, standard library
  only). It copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
  (`/output` inside the grader) and reads it back to check the
  copy, so both grader runs produce the same bytes.
- `LICENSE` — MIT.

## Run it

```sh
python3 draw.py        # renders entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Gate check

- PNG, 1024×1024 pixels, well under the 1 MiB limit.
- No network access and no third-party packages at run time.

---

<sub>Entered on [make.fun](https://make.fun/?ref=mpd17n5r&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
