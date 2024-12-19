#!/usr/bin/env python

from functools import reduce, cache
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re

# https://adventofcode.com/2024/day/19

INPUT_FILENAME = "input19.txt"
# INPUT_FILENAME = "sample19.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

patterns = re.split(r',\s*', data.pop(0))
data.pop(0)


@cache
def can_make_towel(target):
    for pattern in patterns:
        if pattern == target:
            return True
        elif target.startswith(pattern):
            if can_make_towel(target[len(pattern):]):
                return True

    return False

@cache
def towel_combo_counts(target):
    total = 0
    for pattern in patterns:
        if pattern == target:
            total += 1
        elif target.startswith(pattern):
            total += towel_combo_counts(target[len(pattern):])

    return total

print("part1:", len([towel for towel in data if can_make_towel(towel)]))
print("part2:", sum([towel_combo_counts(towel) for towel in data]))
