#!/usr/bin/env python

from functools import reduce

from networkx.classes import neighbors
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re

from aoclib import build_grid, print_grid, Vector, SQUARE_NEIGHBOURS

# https://adventofcode.com/2024/day/12

INPUT_FILENAME = "input12.txt"
# INPUT_FILENAME = "sample12.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

grid = build_grid(data)

islands: dict[str, set[Vector]] = {}
part1 = 0
part2 = 0

for v, c in grid.items():
    islands.setdefault(c, set()).add(v)

for c, vectors in islands.items():
    while vectors:
        island = {vectors.pop()}
        found = True
        while found:
            found = False
            for v in list(island):
                for n in v.square_neighbours():
                    if n in vectors:
                        found = True
                        island.add(n)
                        vectors.discard(n)


        edges = set()

        for v in island:
            for d in SQUARE_NEIGHBOURS:
                n = v + d
                if n in island:
                    continue
                edges.add((v, d))

        part1 += len(island) * len(edges)

        sides = 0
        while edges:
            sides += 1
            v, d = edges.pop()

            d1 = d.rotate_right()
            v1 = v + d1
            while (v1, d) in edges:
                edges.remove((v1, d))
                v1 += d1

            d2 = d.rotate_left()
            v2 = v + d2
            while (v2, d) in edges:
                edges.remove((v2, d))
                v2 += d2


        part2 += len(island) * sides


print("part1:", part1)
print("part2:", part2)
