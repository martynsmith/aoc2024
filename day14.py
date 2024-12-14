#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re
from operator import mul

from aoclib import Vector, print_grid

# https://adventofcode.com/2024/day/14

INPUT_FILENAME = "input14.txt"
MX, MY = 101, 103
# INPUT_FILENAME = "sample14.txt"
# MX, MY = 11, 7

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

bots = []

for line in data:
    px, py, dx, dy = map(int, re.findall(r"-?\d+", line))
    bots.append(
        (
            Vector(px, py),
            Vector(dx, dy),
        )
    )

p1 = {}

for p, d in bots:
    np = p + d * 100
    np = Vector(np.x % MX, np.y % MY)
    qx = 2 * np.x / (MX - 1)
    qy = 2 * np.y / (MY - 1)

    if qx == 1 or qy == 1:
        continue

    if qx == 2:
        qx -= 0.1
    if qy == 2:
        qy -= 0.1

    q = Vector(int(qx), int(qy))
    p1.setdefault(q, 0)
    p1[q] += 1

print('part1:', reduce(mul, p1.values()))

tree_points = set()
for y in range(MY):
    for x in range(max(0, MX // 2 - y), min(MX - 1, MX // 2 + y)):
        tree_points.add(Vector(x, y))

steps = 0
for _ in range(7340):
    bot_points = set(p for p, _ in bots)

    neighbour_count = 0
    for p in bot_points:
        neighbour_count += len(set(p.square_neighbours()).intersection(bot_points))

    # We're just assuming that a Christmas tree will have lots of points next to each other
    if neighbour_count > len(bots):
        print("part2:", steps)
        break

    bots = [(Vector((p.x + d.x) % MX, (p.y + d.y) % MY), d) for p, d in bots]
    steps += 1
