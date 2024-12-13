from dataclasses import dataclass, field

from lib.point import Point


@dataclass(frozen=True)
class Region:
    points: set[Point] = field(default_factory=set)

    def contains(self, p: Point) -> bool:
        return p in self.points

    def area(self) -> int:
        return len(self.points)
