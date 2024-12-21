#!/usr/bin/env python

from functools import reduce

import networkx as nx
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re

from aoclib import build_grid, print_grid, get_bounds, Vector

# https://adventofcode.com/2024/day/20

INPUT_FILENAME = "input20.txt"
# INPUT_FILENAME = "sample20.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

grid: dict[Vector, str | int] = build_grid(data)

start = next(k for k, v in grid.items() if v == 'S')
end = next(k for k, v in grid.items() if v == 'E')

print(f"start: {start}, end: {end}")

# print_grid(grid)

grid[start] = 0
grid[end] = '.'

current_length = 0
by_length = {0: {start}}

while by_length.get(current_length):
    for v in by_length[current_length]:
        for n in v.square_neighbours():
            if grid.get(n) == '.':
                grid[n] = current_length + 1
                by_length.setdefault(current_length + 1, set()).add(n)
            elif isinstance(grid.get(n), int):
                length = min(grid[n], current_length + 1)
                grid[n] = length
                by_length.setdefault(length, set()).add(n)

    current_length += 1

def cheat(from_vector: Vector, ps: int):
    cheats = set()
    for x in range(-ps, ps + 1):
        for y in range(-ps, ps + 1):
            if x == 0 and y == 0:
                continue
            d = Vector(x, y)
            m = abs(d.x) + abs(d.y)
            if m > ps:
                continue
            if not isinstance(grid.get(from_vector + d), int):
                continue

            gain = grid[from_vector + d] - grid[from_vector] - m
            if gain >= 100:
                cheats.add((from_vector, from_vector + d))

    return cheats

all_cheats = set()
for v, c in grid.items():
    if not isinstance(c, int):
        continue
    all_cheats.update(cheat(v, 2))

print('part1:', len(all_cheats))

all_cheats = set()
for v, c in grid.items():
    if not isinstance(c, int):
        continue
    all_cheats.update(cheat(v, 20))

print('part2:', len(all_cheats))

