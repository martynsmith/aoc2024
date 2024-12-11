#!/usr/bin/env python

from functools import cache
from rich import print
from pathlib import Path

# https://adventofcode.com/2024/day/11

INPUT_FILENAME = "input11.txt"
# INPUT_FILENAME = "sample11.txt"

data = list(map(int, Path(INPUT_FILENAME).read_text().split(' ')))

@cache
def blink(n: int, times: int):
    if times == 0:
        return 1

    if n == 0:
        return blink(1, times - 1)

    digits = len(str(n))
    if digits % 2 == 0:
        return blink(n // 10 ** (digits // 2), times - 1) + blink(n % 10 ** (digits // 2), times - 1)

    return blink(n * 2024, times - 1)

print("part1: ", sum([blink(d, 25) for d in data]))
print("part2: ", sum([blink(d, 75) for d in data]))
