#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle, pairwise
from pathlib import Path
from operator import sub
import math
import re

# https://adventofcode.com/2024/day/22

INPUT_FILENAME = "input22.txt"
# INPUT_FILENAME = "sample22.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

def mix(n, s):
    return n ^ s

def prune(s):
    return s % 16777216

part1 = 0
part2 = 0

def calc_next_s(n):
    n = prune(mix(n, n * 64))
    n = prune(mix(n, n // 32))
    n = prune(mix(n, n * 2048))
    return n

part1 = 0

totals = {}
for s in map(int, data):
    diff = []

    prev_v = None
    best = {}

    for i in range(2001):
        next_s = calc_next_s(s)
        v = s % 10

        if prev_v is not None:
            d = (v - prev_v)
            diff.append(d)
            tdiff = tuple(diff[-4:])
            if len(tdiff) == 4 and tdiff not in best:
                best[tdiff] = v

        prev_v = v

        if i == 2000:
            break
        s = next_s

    for combo, value in best.items():
        if combo not in totals:
            totals[combo] = 0
        totals[combo] += value

    part1 += s

print("part1:", part1)

part2 = 0
for combo, value in totals.items():
    if value > part2:
        part2 = value

print("part2:", part2)
