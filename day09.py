#!/usr/bin/env python

from pathlib import Path
# from rich import print

# https://adventofcode.com/2024/day/9

INPUT_FILENAME = "input09.txt"
# INPUT_FILENAME = "sample09.txt"

data = list(map(int, Path(INPUT_FILENAME).read_text().strip()))

part1 = []

head = 0
tail = len(data) - 1
assert tail % 2 == 0
tail_id = None
tail_size = 0

# print("".join(map(str, data)))

while head <= tail:
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

head = 0
tail = len(data) - 1

data = [(i // 2 if i % 2 == 0 else 0, v) for i, v in enumerate(data)]

# print(data)

def render(data):
    out = ""
    for i, count in data:
        if i == 0 and out:
            char = "."
        else:
            char = str(i)

        for _ in range(count):
            out += char
    return out

# print(render(data))

while tail >= 0:
    file_id, file_size = data[tail]

    for i in range(1, tail):
        potential_id, potential_size = data[i]
        if potential_id != 0:
            # only want free space
            continue
        if potential_size >= file_size:
            # print("moving", file_id, "to", i, data[i])
            data[i:i+1] = [(0, 0), (file_id, file_size), (potential_id, potential_size - file_size)]

            # account for the extra entry
            tail += 2

            data[tail-1] = (0, data[tail-1][1] + file_size)
            data[tail] = (0, 0)
            break

    tail -= 2

part2 = 0

block_position = 0
for i, count in data:
    for _ in range(count):
        part2 += block_position * i
        block_position += 1

print("part2:", part2)
print("part2:", part2 == 6286182965311)
