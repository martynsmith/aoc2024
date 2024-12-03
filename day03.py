#!/usr/bin/env python

from pathlib import Path
from operator import mul
import re

# https://adventofcode.com/2024/day/03

INPUT_FILENAME = "input03.txt"
# INPUT_FILENAME = "sample03.txt"

data = Path(INPUT_FILENAME).read_text()

part1 = 0
part2 = 0
part2_active = True

for match in re.findall(r"(mul\(\d+,\d+\)|do\(\)|don\'t\(\))", data):
    if "mul" in match:
        part1 += mul(*map(int, re.findall(r"\d+", match)))

    if "don't" in match:
        part2_active = False
    elif "do" in match:
        part2_active = True
    elif part2_active:
        part2 += mul(*map(int, re.findall(r"\d+", match)))

print("part1:", part1)
print("part2:", part2)
