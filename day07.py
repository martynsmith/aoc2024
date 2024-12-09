#!/usr/bin/env python

from itertools import product
from pathlib import Path

from rich import print

# https://adventofcode.com/2024/day/7

INPUT_FILENAME = "input07.txt"
# INPUT_FILENAME = "sample07.txt"

data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

def check(values, total, target, ops):
    if not values:
        return total == target

    return any([check(values[1:], op(total, values[0]), target, ops) for op in ops])

part1_operations = [
    lambda t, v: t + v,
    lambda t, v: t * v,
]

part2_operations = part1_operations + [
    lambda t, v: int(str(t) + str(v))
]

for line in data:
    result, values = line.split(": ")
    result = int(result)
    values = list(map(int, values.split()))

    if check(values[1:], values[0], result, part1_operations):
        part1 += result

    if check(values[1:], values[0], result, part2_operations):
        part2 += result


print("part1:", part1)
print("part2:", part2)
