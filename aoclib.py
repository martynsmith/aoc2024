from __future__ import annotations
from contextlib import contextmanager
import time
from typing import NamedTuple, Iterable, Callable


@contextmanager
def timer(description):
    start = time.perf_counter_ns()
    yield
    end = time.perf_counter_ns()
    ms = (end - start) / 10 ** 6
    print(f"{description}: {ms}ms")


class Vector(NamedTuple):
    x: int
    y: int

    def __add__(self, p) -> Vector:
        return Vector(self.x + p.x, self.y + p.y)

    def __sub__(self, p) -> Vector:
        return Vector(self.x - p.x, self.y - p.y)

    def __mul__(self, m) -> Vector:
        return Vector(self.x * m, self.y * m)

    def __floordiv__(self, d) -> Vector:
        return Vector(self.x // d, self.y // d)

    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y)

    def rotate_left(self) -> Vector:
        return Vector(self.y, -self.x)

    def rotate_right(self) -> Vector:
        return Vector(-self.y, self.x)

    def square_neighbours(self):
        return [self + v for v in SQUARE_NEIGHBOURS]

    def diagonal_neighbours(self):
        return [self + v for v in DIAGONAL_NEIGHBOURS]

def get_bounds(vectors: Iterable[Vector]) -> (Vector, Vector):
    start = end = None
    for v in vectors:
        if start is None:
            start = v
        if end is None:
            end = v
        start = Vector(min(start.x, v.x), min(start.y, v.y))
        end = Vector(max(end.x, v.x), max(end.y, v.y))

    return start, end


SQUARE_NEIGHBOURS = (
    Vector(0, -1),
    Vector(0, 1),
    Vector(-1, 0),
    Vector(1, 0),
)

DIAGONAL_NEIGHBOURS = SQUARE_NEIGHBOURS + (
    Vector(-1, -1),
    Vector(1, -1),
    Vector(-1, 1),
    Vector(1, 1),
)


def print_grid(cells, default_char=' '):
    minx = min(v.x for v in cells.keys())
    miny = min(v.y for v in cells.keys())
    maxx = max(v.x for v in cells.keys())
    maxy = max(v.y for v in cells.keys())

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print(cells.get(Vector(x, y), default_char), end="")
        print()

def build_grid[T = str](data: list[str], mutator: Callable[[str], T] | None=None) -> dict[Vector, T]:
    grid = {}

    if mutator is None:
        mutator = lambda x: x

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[Vector(x, y)] = mutator(c)

    return grid


class Vector3(NamedTuple):
    x: int
    y: int
    z: int

    def __add__(self, p) -> Vector3:
        return Vector3(self.x + p.x, self.y + p.y, self.z + p.z)

    def get_neighbours(self):
        return [self + v for v in NEIGHBOURS_3]


NEIGHBOURS_3 = (
    Vector3(0, 0, -1),
    Vector3(0, 0, 1),
    Vector3(0, -1, 0),
    Vector3(0, 1, 0),
    Vector3(-1, 0, 0),
    Vector3(1, 0, 0),
)


def get_3d_bounds(vectors: Iterable[Vector3]):
    v1 = list(vectors)[0]

    bounds = [v1.x, v1.x, v1.y, v1.y, v1.z, v1.z]

    for v in vectors:
        bounds[0] = min(bounds[0], v.x)
        bounds[1] = max(bounds[1], v.x)
        bounds[2] = min(bounds[2], v.y)
        bounds[3] = max(bounds[3], v.y)
        bounds[4] = min(bounds[4], v.z)
        bounds[5] = max(bounds[5], v.z)

    return bounds
