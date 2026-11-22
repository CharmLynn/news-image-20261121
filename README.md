# The World in One Day — Saturday, 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/CharmLynn/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/CharmLynn/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A single 1024×1024 front page for 21 November 2026: one lead story
in a coloured panel, four more stories on cards, and the sources
along the bottom. The whole page is drawn by code — no photographs,
no pasted-in artwork.

## What happened that day

- **COP31 talks run into overtime in Antalya.** The climate
  conference misses its Friday deadline: nearly 200 countries are
  deadlocked over a draft deal that says nothing about fossil
  fuels, and a third text is due on Saturday. Sources: Hürriyet
  Daily News, Al Jazeera, Reuters.
- **Mexico captures "El Chapo Isidro".** Army special forces seize
  Fausto Isidro Meza Flores, one of the FBI's ten most wanted, in
  Guasave, Sinaloa. Four soldiers and seven gunmen die in the raid.
  Sources: Reuters, AP, NPR.
- **Russian strike hits Zelensky's home city.** Ballistic missiles
  strike Kryvyi Rih on Friday night, killing a 7-year-old boy and
  a 20-year-old woman and wounding 60 people. Sources: AP, Al
  Jazeera.
- **Drones set Russian cargo ship ablaze.** The Sparta II, sailing
  for Kaliningrad, is hit in the Gulf of Finland and catches fire;
  all 16 crew are evacuated as the ship drifts into Finnish waters.
  Sources: Reuters, Al Jazeera, CNN.
- **Mosquitoes cut dengue by 69% in Brazil trial.** In Belo
  Horizonte, schoolchildren in neighbourhoods with Wolbachia-carrying
  mosquitoes caught far less dengue and chikungunya, researchers
  report. Sources: AP, The Straits Times.

Every story above happened, or was first reported, on 21 November
2026.

## How it is built

`draw.py` paints `entry.png` with Pillow: a paper background, serif
headlines, and five small flat icons drawn from scratch. Running it
twice gives byte-identical output. `main.py` (Python 3.13, standard
library only) copies that image to `$MAKEFUN_OUTPUT_DIR/entry.png`
— `/output` in the grader — and checks the copy's SHA-256, so the
grader's two runs agree. `LICENSE` is MIT.

```sh
python3 draw.py        # render entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The finished PNG is 1024×1024 pixels and well under the 1 MiB cap;
the program needs no network and no third-party packages.

---

<sub>Entered on [make.fun](https://make.fun/?ref=mpd17n5r&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
