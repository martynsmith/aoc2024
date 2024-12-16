#!/usr/bin/env python

from functools import reduce, cache

import networkx as nx
# from rich import print
from itertools import cycle, pairwise
from pathlib import Path
import math
import re

from aoclib import build_grid, print_grid, SQUARE_NEIGHBOURS, Vector

# https://adventofcode.com/2024/day/16

INPUT_FILENAME = "input16.txt"
# INPUT_FILENAME = "sample16.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

grid = build_grid(data)

g = nx.Graph()

start = None
end = None

for v, c in grid.items():
    if c == 'S':
        start = v
    elif c == 'E':
        end = v
    elif c != ".":
        continue

    for d in SQUARE_NEIGHBOURS:
        g.add_node((v, d))
        g.add_edge((v, d), (v, d.rotate_left()), weight=1000)
        g.add_edge((v, d), (v, d.rotate_right()), weight=1000)

        if grid.get(v + d) == '.':
            g.add_edge((v, d), (v + d, d), weight=1)

part1 = None

possible_ends = [(end, d) for d in SQUARE_NEIGHBOURS]
for pe in possible_ends:
    calc = 0
    path = nx.shortest_path(g, (start, Vector(1, 0)), pe, weight='weight')
    path_length = len(path)
    for n1, n2 in pairwise(path):
        calc += g[n1][n2]['weight']
    if part1 is None or calc < part1:
        part1 = calc

print("part1:", part1)

extra_cache = {}

@cache
def fill(v, d, depth=0):
    if extra_cache.get((v, d), part1) < depth:
        return set()

    extra_cache[(v, d)] = depth

    # print(v, d, depth)
    if depth > part1:
        return set()

    if v == end:
        return {v}

    seen = set()
    for nd in d.rotate_left(), d.rotate_right():
        found = fill(v , nd, depth + 1000)
        if found:
            seen.update({v} | found)

    if grid.get(v + d) in {'.', 'E'}:
        found = fill(v + d, d, depth + 1)
        if found:
            seen.update({v} | found)

    return seen

print('part2:', len(fill(start, Vector(1, 0))))
