#!/usr/bin/env python

from rich import print
from pathlib import Path

from aoclib import Vector

# https://adventofcode.com/2024/day/6

INPUT_FILENAME = "input06.txt"
# INPUT_FILENAME = "sample06.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

tl = Vector(0, 0)
br = Vector(len(data[0]), len(data))

obstacles = set()
guard_start = None
direction = None

for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == "#":
            obstacles.add(Vector(x, y))
        if c in {'v', '^', '<', '>'}:
            guard_start = Vector(x, y)
            match c:
                case '^':
                    direction = Vector(0, -1)
                case 'v':
                    direction = Vector(0, 1)
                case '<':
                    direction = Vector(-1, 0)
                case '>':
                    direction = Vector(1, 0)
                case _:
                    raise NotImplemented()


def walk(obstacles, guard, direction):
    visited = set()
    loop_detection = set()

    while guard.x >= tl.x and guard.x < br.x and guard.y >= tl.y and guard.y < br.y:
        visited.add(guard)
        if (guard, direction) in loop_detection:
            return 'LOOP'
        loop_detection.add((guard, direction))
        if guard + direction in obstacles:
            direction = direction.rotate_right()
            continue
        guard += direction

    return visited

part1 = walk(obstacles, guard_start, direction)
print("part1:", len(part1))

part2 = 0

for y in range(br.y):
    for x in range(br.x):
        v = Vector(x, y)
        if v not in part1:
            # If the guard didn't go here originally, an obstacle isn't going to do much good here
            continue
        if walk(obstacles | {v}, guard_start, direction) == 'LOOP':
            part2 += 1


print("part2:", part2)
