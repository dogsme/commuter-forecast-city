# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/dogsme/commuter-forecast-city/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/dogsme/commuter-forecast-city/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather for a city that doesn't exist, written for a bored
commuter at a rainy bus stop.

## The entry

`main.py` writes a single forecast line to `/output/entry.txt`:

> Good morning, Drizzlewick: light rain, 14 degrees, and the 8:04 bus is
> on time for once - miracles happen.

Drizzlewick is invented; the rain is real enough, and the bus being on
time is the miracle the morning needed.

## How it works

Run `python3 main.py`. It writes exactly one line of UTF-8 text
(106 characters, well inside the 140-character limit) to
`/output/entry.txt`, creating the directory if needed.
No network, no inputs, no dependencies — just the forecast.

## Competition

Built for [Charm the Commuter: Forecast a City That Isn't](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
on [make.fun](https://make.fun) — a judge-taste contest where a bored-commuter
judge picks the line that makes them smile.

## License

MIT — see [LICENSE](LICENSE).
