#!/usr/bin/env python
from math import log10
from pathlib import Path
from rich import print
from operator import add, mul

# https://adventofcode.com/2024/day/7

INPUT_FILENAME = "input07.txt"
# INPUT_FILENAME = "sample07.txt"

data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

def check(values, total, target, ops):
    if total > target:
        return False
    if not values:
        return total == target

    tail = values[1:]

    return any((check(tail, op(total, values[0]), target, ops) for op in ops))

part1_operations = (add, mul)

part2_operations = part1_operations + (
    lambda t, v: t * 10 ** len(str(v)) + v,
)

for line in data:
    result, values = line.split(": ")
    result = int(result)
    values = tuple(map(int, values.split()))

    if check(values[1:], values[0], result, part1_operations):
        part1 += result

    if check(values[1:], values[0], result, part2_operations):
        part2 += result


print("part1:", part1)
print("part2:", part2)
