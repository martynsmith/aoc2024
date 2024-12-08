#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle, combinations
from pathlib import Path
import math
import re

from aoclib import print_grid, Vector

# https://adventofcode.com/2024/day/8

INPUT_FILENAME = "input08.txt"
# INPUT_FILENAME = "sample08.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

by_char = {}

tl = Vector(0, 0)
br = Vector(len(data[0]), len(data))

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == '.':
            continue
        v =Vector(x, y)
        by_char.setdefault(char, set())
        by_char[char].add(v)

part1 = set()

for char, nodes in by_char.items():
    for n1,n2 in combinations(nodes, 2):
        part1.add(n1 + (n1 - n2))
        part1.add(n2 + (n2 - n1))

part1 = {n for n in part1 if n.x >= tl.x and n.x < br.x and n.y >= tl.y and n.y < br.y}

part2 = set()

for char, nodes in by_char.items():
    for n1,n2 in combinations(nodes, 2):
        part2.add(n1)
        part2.add(n2)

        d1 = (n1 - n2)
        new1 = n1 + d1
        while new1.x >= tl.x and new1.x < br.x and new1.y >= tl.y and new1.y < br.y:
            part2.add(new1)
            new1 += d1

        d2 = (n2 - n1)
        new2 = n2 + d2
        while new2.x >= tl.x and new2.x < br.x and new2.y >= tl.y and new2.y < br.y:
            part2.add(new2)
            new2 += d2

# printable = {}
# for char, nodes in by_char.items():
#     for node in nodes:
#         printable[node] = char
# for node in part2:
#     printable[node] = '#'
# print_grid(printable, ' ')

print("part1:", len(part1))
print("part2:", len(part2))
