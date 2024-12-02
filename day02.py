#!/usr/bin/env python

from itertools import pairwise
from functools import reduce
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re

# https://adventofcode.com/2024/day/2

INPUT_FILENAME = "input02.txt"
# INPUT_FILENAME = "sample02.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

def is_safe(line: list[int]) -> bool:
    l1 = sorted(line)
    l2 = sorted(line, reverse=True)
    diffs = {abs(a-b) for a, b in pairwise(line)}
    return diffs.issubset({1, 2, 3}) and (line == l1 or line == l2)

for line in data:
    line = list(map(int, line.split()))
    if is_safe(line):
        part1 += 1
        part2 += 1
    elif any(is_safe(line[:i] + line[i+1:]) for i in range(len(line))):
        part2 += 1


print("part1:", part1)
print("part2:", part2)
