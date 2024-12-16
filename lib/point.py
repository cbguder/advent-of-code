from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, fac: int) -> Point:
        return Point(self.x * fac, self.y * fac)
