#!/usr/bin/env python

from rich import print
from pathlib import Path
from aoclib import Vector, DIAGONAL_NEIGHBOURS, build_grid

# https://adventofcode.com/2024/day/4

INPUT_FILENAME = "input04.txt"
# INPUT_FILENAME = "sample04.txt"


# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

grid = build_grid(data)

x1 = (Vector(-1, -1), Vector(1, 1))
x2 = (Vector(1, -1), Vector(-1, 1))

for p, c in grid.items():
    for d in DIAGONAL_NEIGHBOURS:
        if all(grid.get(p + d * index) == char for index, char in enumerate("XMAS")):
            part1 += 1

    if c == 'A':
        if set(grid.get(p + x) for x in x1) == set(grid.get(p + x) for x in x2) == {'M', 'S'}:
            part2 += 1

print("part1:", part1)
print("part2:", part2)
