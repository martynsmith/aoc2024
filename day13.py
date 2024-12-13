#!/usr/bin/env python

from functools import reduce

import networkx as nx
from rich import print
from itertools import pairwise
from pathlib import Path
import re

from aoclib import Vector

# https://adventofcode.com/2024/day/13

INPUT_FILENAME = "input13.txt"
# INPUT_FILENAME = "sample13.txt"

# data = Path(INPUT_FILENAME).read_text()
games = [line.strip() for line in Path(INPUT_FILENAME).read_text().split('\n\n')]


part1 = 0
part2 = 0

for line in games:
    g = nx.Graph()

    ax, ay = map(int, re.search('Button A: X\+(\d+), Y\+(\d+)', line).groups())
    bx, by = map(int, re.search('Button B: X\+(\d+), Y\+(\d+)', line).groups())
    px, py = map(int, re.search('Prize: X=(\d+), Y=(\d+)', line).groups())

    px += 10000000000000
    py += 10000000000000

    a = Vector(ax, ay)
    b = Vector(bx, by)

    v = Vector(0, 0)
    g.add_node(v)
    print(1)
    while v.x < px or v.y < py:
        nv = Vector(v.x+ax, v.y+ay)
        g.add_edge(v, nv, weight=3)
        v = nv

    v = Vector(px, py)
    print(2)
    while v.x > 0 or v.y > 0:
        nv = Vector(v.x-ax, v.y-ay)
        g.add_edge(v, nv, weight=3)
        v = nv

    v = Vector(0, 0)
    print(3)
    while v.x < px or v.y < py:
        nv = Vector(v.x+bx, v.y+by)
        g.add_edge(v, nv, weight=1)
        v = nv

    v = Vector(px, py)
    print(4)
    while v.x > 0 or v.y > 0:
        nv = Vector(v.x-bx, v.y-by)
        g.add_edge(v, nv, weight=1)
        v = nv

    a_count = 0
    b_count = 0
    print(5)
    try:
        for x, y in pairwise(nx.shortest_path(g, Vector(0, 0), Vector(px, py))):
            if y - x == a:
                a_count += 1
            elif y - x == b:
                b_count += 1
            else:
                raise(Exception())
        part1 += a_count * 3 + b_count
    except nx.NetworkXNoPath:
        pass

print("part1:", part1)
# print("part2:", part2)
