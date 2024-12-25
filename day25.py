#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle, product
from pathlib import Path
import math
import re

# https://adventofcode.com/2024/day/25

INPUT_FILENAME = "input25.txt"
# INPUT_FILENAME = "sample25.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().split('\n\n')]

part1 = 0
part2 = 0

locks = set()
keys = set()

for line in data:
    type = 'lock'

    if line.startswith('.'):
        type = 'key'

    if type == 'lock':
        header = line.splitlines()[0]
        body = line.splitlines()[1:]
        lock_height = len(body)
    else:
        header = line.splitlines()[-1]
        body = reversed(line.splitlines()[:-1])

    heights = [0] * len(line.splitlines()[0])
    for l in line.splitlines()[1:]:
        for i, c in enumerate(l):
            if c == '#':
                heights[i] += 1

    if type == 'key':
        heights = [h-1 for h in heights]
        keys.add(tuple(heights))
    else:
        locks.add((lock_height, tuple(heights)))

part1 = 0
for (lock_height, lock), key in product(locks, keys):
    # print(lock, key)
    if max(l + k for l, k in zip(lock, key)) < lock_height:
        part1 += 1

print("part1:", part1)
# print("part2:", part2)
