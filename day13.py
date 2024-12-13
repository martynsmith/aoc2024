#!/usr/bin/env python

from functools import reduce

import networkx as nx
from rich import print
from itertools import pairwise
from pathlib import Path
import math
import re
from sympy import symbols, Eq, solve, diophantine, simplify

from aoclib import Vector

# https://adventofcode.com/2024/day/13

INPUT_FILENAME = "input13.txt"
# INPUT_FILENAME = "sample13.txt"


games = [line.strip() for line in Path(INPUT_FILENAME).read_text().split('\n\n')]

part1 = 0
part2 = 0
a, b, x, y = symbols('a b x y')

for line in games:
    ax, ay = map(int, re.search(r'Button A: X\+(\d+), Y\+(\d+)', line).groups())
    bx, by = map(int, re.search(r'Button B: X\+(\d+), Y\+(\d+)', line).groups())
    px, py = map(int, re.search(r'Prize: X=(\d+), Y=(\d+)', line).groups())

    lhs = a * (ax * x + ay * y) + b * (bx * x + by * y)
    rhs  = px * x + py * y
    equation = Eq(lhs, rhs)
    solution = solve(equation, (a, b))
    if solution[a].is_integer and solution[b].is_integer:
        part1 += solution[a] * 3 + solution[b]

    px += 10000000000000
    py += 10000000000000

    lhs = a * (ax * x + ay * y) + b * (bx * x + by * y)
    rhs  = px * x + py * y
    equation = Eq(lhs, rhs)
    solution = solve(equation, (a, b))
    if solution[a].is_integer and solution[b].is_integer:
        part2 += solution[a] * 3 + solution[b]

print("part1:", part1)
print("part2:", part2)
