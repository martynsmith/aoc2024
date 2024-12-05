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

part1 = 0
part2 = 0

rule_pairs = [list(map(int, line.split('|'))) for line in rules.splitlines()]

def check(update):
    for x, y in rule_pairs:
        if x not in update or y not in update:
            continue
        if update.index(x) > update.index(y):
            return False
    return True

def do_sort(update):
    while not check(update):
        for x, y in rule_pairs:
            if x not in update or y not in update:
                continue
            ix = update.index(x)
            iy = update.index(y)
            if ix > iy:
                update[iy], update[ix] = update[ix], update[iy]
    return update

for update in updates.splitlines():
    update = list(map(int, update.split(',')))

    if check(update):
        part1 += update[len(update)//2]
    else:
        update = do_sort(update)
        part2 += update[len(update)//2]


print("part1:", part1)
print("part2:", part2)
