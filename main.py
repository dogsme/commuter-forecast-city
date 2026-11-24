#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for a
city that does not exist, to /output/entry.txt.
"""

import os

FORECAST = (
    "Good morning, Drizzlewick: light rain, 14 degrees, and the 8:04 bus "
    "is on time for once - miracles happen."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST + "\n")


if __name__ == "__main__":
    main()
