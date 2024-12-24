#!/usr/bin/env python

from functools import reduce
from rich import print
from itertools import cycle, combinations, zip_longest
from pathlib import Path
import math
import re

# https://adventofcode.com/2024/day/24

INPUT_FILENAME = "input24.txt"
# INPUT_FILENAME = "sample24.txt"

# data = Path(INPUT_FILENAME).read_text()
data = [line.strip() for line in Path(INPUT_FILENAME).read_text().splitlines()]

part1 = 0
part2 = 0

wires = {}

for line in data:
    if match := re.search(r'(\S+): ([01])', line):
        wires[match.group(1)] = int(match.group(2))
    elif match := re.search(r'(\S+) (OR|XOR|AND) (\S+) -> (\S+)', line):
        o1, op, o2, out = match.groups()
        wires[out] = (o1, op, o2)

def get_number(wires, letter):
    matching_wires = sorted((k for k in wires.keys() if k.startswith(letter)), reverse=True)


    result = 0
    for wire in matching_wires:
        result = result * 2 + wires[wire]

    return result

def solve(wires):
    wires = wires.copy()

    while True:
        matched = False
        for wire, value in list(wires.items()):
            if isinstance(value, int):
                continue

            o1, op, o2 = value
            if not isinstance(wires[o1], int) or not isinstance(wires[o2], int):
                continue

            matched = True
            match op:
                case 'AND':
                    wires[wire] = wires[o1] & wires[o2]
                case 'OR':
                    wires[wire] = wires[o1] | wires[o2]
                case 'XOR':
                    wires[wire] = wires[o1] ^ wires[o2]
                case _:
                    raise NotImplementedError()

        if not matched:
            break

    return get_number(wires, 'z')

print("part1:", solve(wires))

def find_interesting(matches: set[str]):
    results = []
    for wire, value in wires.items():
        if isinstance(value, int):
            continue

        o1, op, o2 = value
        if o1 in matches or o2 in matches:
            results.append((op, o1, o2, wire))

    return sorted(results)

i = 0
c_in = None
for x, y, z in zip_longest(
    sorted((k for k in wires.keys() if k.startswith('x'))),
    sorted((k for k in wires.keys() if k.startswith('y'))),
    sorted((k for k in wires.keys() if k.startswith('z'))),
):
    print(x, y, z, c_in)
    layer1 = find_interesting({x, y, z})
    assert len(layer1) == 2

    assert tuple(layer1[0][:3]) in {('AND', x, y), ('AND', y, x)}
    if c_in is None:
        assert layer1[1] == ('XOR', x, y, z)
        a_and_b = layer1[0][3]
        c_in = layer1[0][3]
    else:
        assert tuple(layer1[1][:3]) in {('XOR', x, y), ('XOR', y, x)}
        a_and_b = layer1[0][3]
        a_xor_b = layer1[1][3]
        print(f"{layer1=} {a_and_b=} {a_xor_b=} {c_in=}")
        layer2 = find_interesting({a_and_b, a_xor_b})
        c_in_and_a_xor_b = layer2[0][3]
        print(f"{layer2=} {c_in_and_a_xor_b=}")

        assert len(layer2) == 3

        assert tuple(layer2[0][:3]) in {('AND', a_xor_b, c_in), ('AND', c_in, a_xor_b)}
        assert tuple(layer2[1][:3]) in {('OR', a_and_b, c_in_and_a_xor_b), ('OR', c_in_and_a_xor_b, a_and_b)}
        assert layer2[2] in {('XOR', a_xor_b, c_in, z), ('XOR', c_in, a_xor_b, z)}

        c_in = layer2[1][3]

        # layer3 = find_interesting({a_and_b})
        # print(f"{layer3=}")
        # assert len(layer1) == 2
        # assert len(layer3) == 1
        # assert tuple(layer3[0][:3]) in {('OR', a_and_b, c_in_and_a_xor_b), ('OR', c_in_and_a_xor_b, a_and_b)}
        # c_in = layer3[0][3]
        # print(c_in)
        # print('layer3:', layer3)

    if x == 'x10':
        break
    print('------------------------')
