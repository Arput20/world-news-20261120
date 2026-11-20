[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Arput20/world-news-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard)
[![reward](https://make.fun/badge/news-image-20261120/Arput20/world-news-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

# World News 20261120

A comprehensive, illustrated front-page layout for November 20, 2026, created for the make.fun news image bounty. This project compiles global headlines—ranging from historic trilateral summits to geopolitical developments and market shifts—into a high-resolution graphical front page (`entry.png`).

## Components

- **`render_news.py`**: Python script utilizing Pillow (PIL) to generate the polished 1024x1024 front-page graphic (`entry.png`) featuring multi-panel layouts, custom typography, icons, and market digests.
- **`bot_main.ts` / `main.ts`**: TypeScript automation script that safely and atomically delivers `entry.png` to the deployment destination directory.

## Running the Output Program

To test the distribution process locally and export the generated front-page image to a custom directory:

```sh
MAKEFUN_OUTPUT_DIR=out node main.ts
```

Set the `MAKEFUN_BOT_DIR` environment variable if your assets reside in a non-standard directory.

## License

MIT
