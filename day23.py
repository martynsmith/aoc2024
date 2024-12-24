#!/usr/bin/env python

from functools import reduce

import networkx as nx
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re

# https://adventofcode.com/2024/day/23

INPUT_FILENAME = "input23.txt"
# INPUT_FILENAME = "sample23.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

# g = nx.Graph()

edges = {}
nodes = set()
groups = set()

for line in data:
    n1, n2 = line.split('-')
    n1, n2 = sorted([n1, n2])
    edges.setdefault(n1, set()).add(n2)
    edges.setdefault(n2, set()).add(n1)
    nodes.add(n1)
    nodes.add(n2)
    groups.add(tuple(sorted([n1, n2])))

# part1 = set()
#
# for n1, connections in edges.items():
#     for n2 in connections:
#         for n3 in nodes:
#             n3_connections = edges.get(n3, set())
#             if n1 in n3_connections and n2 in n3_connections:
#                 if n1.startswith('t') or n2.startswith('t') or n3.startswith('t'):
#                     part1.add(tuple(sorted([n1, n2, n3])))
#
# print(len(part1))

def grow(groups):
    new_groups = set()
    for group in groups:
        for n in reduce(lambda a, b: a.intersection(b), [edges.get(c, set()) for c in group]):
            new_groups.add(tuple(sorted(list(group) + [n])))
    return new_groups

while True:
    new_groups = grow(groups)
    if not new_groups:
        break
    groups = new_groups

assert len(groups) == 1
print("part2:", ",".join(sorted(list(groups)[0])))

