#!/usr/bin/env python

# from rich import print
from pathlib import Path
import re

# https://adventofcode.com/2024/day/03

INPUT_FILENAME = "input03.txt"
# INPUT_FILENAME = "sample03.txt"

data = Path(INPUT_FILENAME).read_text()

part1 = 0
for match in re.findall(r"mul\((\d+),(\d+)\)", data):
    x, y = map(int, match)
    part1 += x * y

part2 = 0
part2_active = True
for is_mul, x, y, is_do, is_dont in re.findall(
    r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)", data
):
    if is_do:
        part2_active = True
    if is_dont:
        part2_active = False
    if is_mul:
        if part2_active:
            part2 += int(x) * int(y)

print("part1:", part1)
print("part2:", part2)
