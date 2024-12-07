#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle, permutations, combinations, product
from pathlib import Path
import math
import re

# https://adventofcode.com/2024/day/7

INPUT_FILENAME = "input07.txt"
# INPUT_FILENAME = "sample07.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

for line in data:
    result, values = line.split(": ")
    result = int(result)
    values = list(map(int, values.split()))

    for combo in product("+*", repeat=len(values)-1):
        total = values[0]

        for op, value in zip(combo, values[1:]):
            match op:
                case "+":
                    total += value
                case "*":
                    total *= value

        if total == result:
            part1 += total
            break

    for combo in product("+*|", repeat=len(values)-1):
        total = values[0]

        for op, value in zip(combo, values[1:]):
            match op:
                case "+":
                    total += value
                case "*":
                    total *= value
                case '|':
                    total = int(str(total) + str(value))

        if total == result:
            part2 += total
            break


    # print(result, values)

print("part1:", part1)
print("part2:", part2)
