#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re

from aoclib import print_grid, Vector

# https://adventofcode.com/2024/day/10

INPUT_FILENAME = "input10.txt"
# INPUT_FILENAME = "sample10.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

grid = {}

for y, line in enumerate(data):
    for x, c in enumerate(line):
        grid[Vector(x, y)] = int(c)

def calc_part1(v) -> set[Vector]:
    if v in grid and grid[v] == 9:
        return set([v])

    total = set()
    for p in v.square_neighbours():
        if p in grid and grid[p] == grid[v] + 1:
            total |= calc_part1(p)

    return total

def calc_part2(v) -> int:
    if v in grid and grid[v] == 9:
        return 1

    total = 0
    for p in v.square_neighbours():
        if p in grid and grid[p] == grid[v] + 1:
            total += calc_part2(p)

    return total

for v, height in grid.items():
    if height == 0:
        part1 += len(calc_part1(v))
        part2 += calc_part2(v)

# print()
# print_grid(grid)
# print()

print("part1:", part1)
print("part2:", part2)
