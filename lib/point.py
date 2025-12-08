from __future__ import annotations

import math
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

    def __abs__(self) -> Point:
        return Point(abs(self.x), abs(self.y))

    def distance(self, other: Point) -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)


@dataclass(frozen=True, order=True)
class Point3D:
    x: int
    y: int
    z: int

    def __add__(self, other: Point3D) -> Point3D:
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Point3D) -> Point3D:
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, fac: int) -> Point3D:
        return Point3D(self.x * fac, self.y * fac, self.z * fac)

    def __abs__(self) -> Point3D:
        return Point3D(abs(self.x), abs(self.y), abs(self.z))

    def distance(self, other: Point3D) -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)
