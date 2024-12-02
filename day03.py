#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle
from pathlib import Path
import math
import re

# https://adventofcode.com/2024/day/03

INPUT_FILENAME = "input03.txt"
INPUT_FILENAME = "sample03.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

for line in data:
    print(line)

# print("part1:", part1)
# print("part2:", part2)