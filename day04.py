#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re
from aoclib import Vector, print_grid, DIAGONAL_NEIGHBOURS

# https://adventofcode.com/2024/day/4

INPUT_FILENAME = "input04.txt"
# INPUT_FILENAME = "sample04.txt"


# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

grid = {}
for y, line in enumerate(data):
    for x, char in enumerate(line):
        grid[Vector(x, y)] = char

# print_grid(grid)

def find_xmas(pos, letters="XMAS", direction=None):
    if grid[pos] != letters[0]:
        return 0

    if len(letters) == 1:
        if grid[pos] == letters:
            return 1
        else:
            return 0

    total = 0
    if direction is None:
        for direction in DIAGONAL_NEIGHBOURS:
            if pos + direction not in grid:
                continue
            total += find_xmas(pos + direction, letters[1:], direction)
    elif pos + direction in grid:
        total += find_xmas(pos + direction, letters[1:], direction)
    return total


for key in grid.keys():
    part1 += find_xmas(key)

for key in grid.keys():
    if grid[key] != "A":
        continue

    neighbours = [
        Vector(-1, -1),
        Vector(1, -1),
        Vector(-1, 1),
        Vector(1, 1),
    ]

    exists = True

    for n in neighbours:
        if key + n not in grid:
            exists = False

    if not exists:
        continue

    letters = "".join([grid[key + n] for n in neighbours])
    if letters in {
        "MMSS",
        "SMSM",
        "SSMM",
        "MSMS",
    }:
        part2 += 1



print("part1:", part1)
print("part2:", part2)
