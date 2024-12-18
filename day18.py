#!/usr/bin/env python

from functools import reduce

import networkx as nx
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re

from aoclib import Vector, print_grid

# https://adventofcode.com/2024/day/18

INPUT_FILENAME = "input18.txt"
SIZE = 70

# INPUT_FILENAME = "sample18.txt"
# SIZE = 6

data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

all_blocks = [
    Vector(*map(int, re.findall(r'(\d+)', line))) for line in data
]

part1 = 0
part2 = 0

blocks = set()

def build_graph(block_count):
    blocks = set(all_blocks[:block_count])

    g = nx.Graph()

    for y in range(SIZE + 1):
        for x in range(SIZE + 1):
            v = Vector(x, y)
            if v in blocks:
                continue
            for n in v.square_neighbours():
                if n in blocks:
                    continue
                if n.x < 0 or n.y < 0 or n.x > SIZE or n.y > SIZE:
                    continue
                g.add_edge(v, n)
    try:
        return len(nx.shortest_path(g, Vector(0, 0), Vector(SIZE, SIZE))) - 1
    except:
        return -1

print('part1:', build_graph(1024))
i = 1024
while True:
    i += 1
    if build_graph(i) == -1:
        block = all_blocks[i - 1]
        print("part2:", f"{block.x},{block.y}")
        break
