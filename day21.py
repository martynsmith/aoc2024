#!/usr/bin/env python
import re
from functools import cache
from itertools import pairwise, permutations, product

import networkx as nx
from rich import print
from pathlib import Path

from aoclib import Vector, build_grid

# https://adventofcode.com/2024/day/21

INPUT_FILENAME = "input21.txt"
# INPUT_FILENAME = "sample21.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

numeric_keypad_grid= build_grid(["789", "456", "123", " 0A"])

numeric_keypad = nx.DiGraph()
for v, char in numeric_keypad_grid.items():
    if char == " ":
        continue
    for n in v.square_neighbours():
        nchar = numeric_keypad_grid.get(n)
        if nchar is None:
            continue
        direction = {
            Vector(0, 1): "v",
            Vector(0, -1): "^",
            Vector(1, 0): ">",
            Vector(-1, 0): "<",
        }[ n - v ]

        numeric_keypad.add_edge(char, nchar, direction=direction)

direction_keypad = nx.DiGraph()
direction_keypad.add_edge("^", "A", direction=">")
direction_keypad.add_edge("A", "^", direction="<")
direction_keypad.add_edge("<", "v", direction=">")
direction_keypad.add_edge("v", "<", direction="<")
direction_keypad.add_edge("v", ">", direction=">")
direction_keypad.add_edge(">", "v", direction="<")
direction_keypad.add_edge("^", "v", direction="v")
direction_keypad.add_edge("v", "^", direction="^")
direction_keypad.add_edge("A", ">", direction="v")
direction_keypad.add_edge(">", "A", direction="^")

@cache
def find_path(graph, start, end):
    paths = nx.all_shortest_paths(graph, start, end)
    paths = ["".join([graph[n1][n2]['direction'] for n1, n2 in pairwise(path)]) for path in paths]
    return paths

@cache
def type_code(graph, code, start='A'):
    path_segments = []

    for c in code:
        path_segments.append(list(find_path(graph, start, c)))
        start = c

    paths = [
        "A".join(p) + "A" for p in
        product(*path_segments)
    ]

    repeats_map = [len(re.findall(r'(.)\1+', p)) for p in paths]
    max_repeats = max(repeats_map)

    return [p for i, p in enumerate(paths) if repeats_map[i] == max_repeats]

# print(find_path(numeric_keypad, 'A', '0'))

part1 = 0
for target in data:
    shortest_code = None
    for code in type_code(numeric_keypad, target):
        for dcode in type_code(direction_keypad, code, start='A'):
            for dcode2 in type_code(direction_keypad, dcode, start='A'):
                if shortest_code is None or len(dcode2) < len(shortest_code):
                    shortest_code = dcode2

    part1 += len(shortest_code) * int(target.replace('A', ''))

print("part1:", part1)
