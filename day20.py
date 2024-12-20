#!/usr/bin/env python

from functools import reduce

import networkx as nx
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re

from aoclib import build_grid, print_grid

# https://adventofcode.com/2024/day/20

INPUT_FILENAME = "input20.txt"
# INPUT_FILENAME = "sample20.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

grid = build_grid(data)

g = nx.Graph()
for v, c in grid.items():
    if c == 'S':
        start = v
    if c == 'E':
        end = v

    if c == '#':
        continue
    else:
        g.add_node(v)
        for n in v.square_neighbours():
            if grid.get(n) in {'.', 'S', 'E'}:
                g.add_edge(v, n)

base_length = nx.shortest_path_length(g, start, end)
print(base_length)

part1 = 0

for v, c in grid.items():
    if c != '#':
        continue
    for n in v.square_neighbours():
        g.add_edge(v, n)

    saving = base_length - nx.shortest_path_length(g, start, end)

    if saving >= 100:
        part1 += 1

    for n in v.square_neighbours():
        g.remove_edge(v, n)


print("part1:", part1)
# print("part2:", part2)
