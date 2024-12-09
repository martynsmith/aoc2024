#!/usr/bin/env python

from functools import reduce
from itertools import cycle
from pathlib import Path
# from rich import print
import math
import re

# https://adventofcode.com/2024/day/9

INPUT_FILENAME = "input09.txt"
# INPUT_FILENAME = "sample09.txt"

data = list(map(int, Path(INPUT_FILENAME).read_text().strip()))

part1 = []
part2 = 0

head = 0
tail = len(data) - 1
assert tail % 2 == 0
tail_id = None
tail_size = 0

# print(data)

while head <= tail:
    file_size = data

    if head % 2 == 0:
        # this is a file
        # print("file:", data[head])
        for i in range(data[head]):
            file_id = head // 2
            part1.append(file_id)
    else:
        # this is blank space
        # print("blank:", data[head])
        for i in range(int(data[head])):
            if tail_size == 0:
                tail_id = tail // 2
                tail_size = data[tail]
                tail -= 2

            part1.append(tail_id)
            # print(tail_id, end="")
            tail_size -= 1

        pass

    head += 1


while tail_size:
    # print(tail_id, end="")
    part1.append(tail_id)
    tail_size -= 1

# print("\n")

print("part1:", sum([i * v for i, v in enumerate(part1)]))
# print("part2:", part2)
