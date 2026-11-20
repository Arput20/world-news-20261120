[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Arput20/world-news-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard)
[![reward](https://make.fun/badge/news-image-20261120/Arput20/world-news-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

# The world in one day — 20 November 2026

An illustrated "front page" for 20 November 2026, generated for the make.fun
news-image bounty. `entry.png` is the finished artwork; `render_news.py`
produces it locally (PIL + DejaVu fonts) and `main.ts` is the bot entrypoint
that copies `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`)
atomically.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=out node main.ts   # copies entry.png into ./out
```

Set `MAKEFUN_BOT_DIR` if `main.ts` is invoked from another location.

## License

MIT
