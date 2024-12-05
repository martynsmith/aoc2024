#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle
from pathlib import Path
import networkx as nx
import math
import re

# https://adventofcode.com/2024/day/5

INPUT_FILENAME = "input05.txt"
# INPUT_FILENAME = "sample05.txt"

rules, updates = Path(INPUT_FILENAME).read_text().split('\n\n')
rule_pairs = [list(map(int, line.split('|'))) for line in rules.splitlines()]

part1 = 0
part2 = 0


for update in updates.splitlines():
    update = list(map(int, update.split(',')))
    dg = nx.DiGraph()
    for x, y in rule_pairs:
        if x in update and y in update:
            dg.add_edge(x, y)
    index_map = {n: i for i, n in enumerate(nx.topological_sort(dg))}
    update_indexes = [index_map[n] for n in update]
    if update_indexes == sorted(update_indexes):
        part1 += update[len(update)//2]
    else:
        update = sorted(update, key=lambda x: index_map[x])
        part2 += update[len(update)//2]

print("part1:", part1)
print("part2:", part2)
