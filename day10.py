#!/usr/bin/env python

from rich import print
from pathlib import Path

from aoclib import Vector, build_grid

# https://adventofcode.com/2024/day/10

INPUT_FILENAME = "input10.txt"
# INPUT_FILENAME = "sample10.txt"

data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

grid = build_grid(data, int)

def walk(position: Vector, start: Vector | None = None) -> list[tuple[Vector, Vector]]:
    "Returns a list of tuples of the start/end of each trail"

    if start is None:
        start = position

    if position in grid and grid[position] == 9:
        return list([(start, position)])

    total = list()
    for p in position.square_neighbours():
        if p in grid and grid[p] == grid[position] + 1:
            total += walk(p, start)

    return total

trail_ends = []

for v, height in grid.items():
    if height == 0:
        trail_ends += walk(v)

print("part1:", len(set(trail_ends)))
print("part2:", len(trail_ends))
