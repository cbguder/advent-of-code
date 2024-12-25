from dataclasses import dataclass

from lib.point import Point


@dataclass
class Region:
    points: set[Point]

    def contains(self, p: Point) -> bool:
        return p in self.points

    def area(self) -> int:
        return len(self.points)
