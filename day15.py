#!/usr/bin/env python

from rich import print
from pathlib import Path

from aoclib import build_grid, Vector

# https://adventofcode.com/2024/day/15

INPUT_FILENAME = "input15.txt"
# INPUT_FILENAME = "sample15.txt"

warehouse_str, directions_str = Path(INPUT_FILENAME).read_text().split('\n\n')

p1_warehouse = build_grid(warehouse_str.splitlines())
p2_warehouse = build_grid(
    warehouse_str
    .replace('#', '##')
    .replace('O', '[]')
    .replace('.', '..')
    .replace('@', '@.')
    .splitlines()
)

directions = [
    {
        'v': Vector(0, 1),
        '^': Vector(0, -1),
        '>': Vector(1, 0),
        '<': Vector(-1, 0),
    }[c] for c in directions_str.replace('\n', '')
]

p1_position = next(coord for coord, item in p1_warehouse.items() if item == '@')
p2_position = next(coord for coord, item in p2_warehouse.items() if item == '@')



def get_coords_to_move(position, direction, warehouse) -> set[Vector]:
    match warehouse[position + direction]:
        case '.':
            return {position}
        case '#':
            return set()
        case 'O':
            # part 1 logic
            moves = get_coords_to_move(position + direction, direction, warehouse)
            if moves:
                return {position} | moves
            return set()
        case '[' | ']':
            # part 2 logic
            m1 = get_coords_to_move(position + direction, direction, warehouse)
            if direction.y:  # only for vertical movement do we need to account for the block width
                m2 = get_coords_to_move(Vector(position.x + (1 if warehouse[position + direction] == '[' else -1), position.y) + direction, direction, warehouse)
                if m1 and m2:
                    return {position} | m1 | m2
                else:
                    return set()
            elif m1:
                return {position} | m1
            else:
                return set()

    raise NotImplementedError(f"{warehouse[position + direction]=}")

def update_warehouse(position, direction, warehouse):
    moves = get_coords_to_move(position, direction, warehouse)
    if moves:
        # Update the warehouse to be:
        # existing warehouse + '.' for all moving tiles + the new position for all the moving tiles
        return (
            warehouse
            | {v: '.' for v in moves}
            | {v + direction: warehouse[v] for v in moves}
        ), position + direction
    return warehouse, position

for d in directions:
    p1_warehouse, p1_position = update_warehouse(p1_position, d, p1_warehouse)
    p2_warehouse, p2_position = update_warehouse(p2_position, d, p2_warehouse)

def score(warehouse):
    return sum(100 * v.y + v.x for v, item in warehouse.items() if item in {'O', '['})


print("part1:", score(p1_warehouse))
print("part2:", score(p2_warehouse))
