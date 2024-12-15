#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re

from aoclib import build_grid, print_grid, Vector

# https://adventofcode.com/2024/day/15

INPUT_FILENAME = "input15.txt"
INPUT_FILENAME = "sample15.txt"

data = Path(INPUT_FILENAME).read_text().split('\n\n')
# data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

warehouse = build_grid(data[0].splitlines())

position = None
for coord, item in warehouse.items():
    if item == '@':
        position = coord
        # warehouse[coord] = '.'
        break

direction_map = {
    'v': Vector(0, 1),
    '^': Vector(0, -1),
    '>': Vector(1, 0),
    '<': Vector(-1, 0),
}


# print_grid(warehouse)

for direction_str in data[1].strip():
    if direction_str == "\n":
        continue
    # print(direction_str)
    d = direction_map[direction_str]

    search_position = position + d
    while warehouse[search_position] == 'O':
        search_position += d

    match warehouse[search_position]:
        case '.':
            while search_position != position:
                warehouse[search_position] = warehouse[search_position - d]
                search_position -= d
            warehouse[position] = '.'
            position += d
        case '#':
            pass
        case _:
            print(f"{direction_str=}")
            print(f"{position=}")
            print(f"{search_position=}")
            print_grid(warehouse)
            raise NotImplementedError(f"Unexpected character: {warehouse[search_position]}")

part1 = 0
for coord, item in warehouse.items():
    if item == 'O':
        part1 += 100 * coord.y + coord.x

print_grid(warehouse)

print("part1:", part1)
# print("part2:", part2)
