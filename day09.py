#!/usr/bin/env python
from dataclasses import dataclass
from itertools import zip_longest
from pathlib import Path
from rich import print

# https://adventofcode.com/2024/day/9

INPUT_FILENAME = "input09.txt"
# INPUT_FILENAME = "sample09.txt"

@dataclass
class File:
    id: int
    size: int

@dataclass
class Sector:
    initial_file: File | None
    additional_files: list[File]
    free: int


data = list(map(int, Path(INPUT_FILENAME).read_text().strip()))

def part2():
    sectors = [
        Sector(
            initial_file=File(file_id, file),
            additional_files=[],
            free=(free or 0),
        )
        for file_id, (file, free) in
        enumerate(zip_longest(data[::2], data[1::2]))
    ]

    min_free_index = 0

    for source_index in range(len(sectors)-1, -1, -1):
        source = sectors[source_index]
        for target_index in range(min_free_index, source_index):
            target = sectors[target_index]
            if target.free >= source.initial_file.size:
                target.free -= source.initial_file.size
                target.additional_files.append(source.initial_file)

                if source.additional_files:
                    sectors[source_index - 1].free += source.initial_file.size
                else:
                    source.free += source.initial_file.size

                source.initial_file = None
                break
            if target_index == min_free_index and target.free == 0:
                min_free_index += 1


    part2 = 0
    block_position = 0
    for sector in sectors:
        if sector.initial_file:
            sector.additional_files.insert(0, sector.initial_file)
        for file in sector.additional_files:
            part2 += file.id * ((file.size * block_position) + (file.size * (file.size - 1)) // 2)
            block_position += file.size
        block_position += sector.free


    print('part2:', part2)

def part1():
    part1 = []

    head = 0
    tail = len(data) - 1
    assert tail % 2 == 0
    tail_id = None
    tail_size = 0

    while head <= tail:
        if head % 2 == 0:
            # this is a file
            for i in range(data[head]):
                file_id = head // 2
                part1.append(file_id)
        else:
            # this is blank space
            for i in range(int(data[head])):
                if tail_size == 0:
                    tail_id = tail // 2
                    tail_size = data[tail]
                    tail -= 2

                part1.append(tail_id)
                tail_size -= 1

            pass

        head += 1


    while tail_size:
        part1.append(tail_id)
        tail_size -= 1

    print("part1:", sum([i * v for i, v in enumerate(part1)]))

part1()
part2()
