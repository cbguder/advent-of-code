from dataclasses import dataclass, field
from typing import Generator, Optional, Tuple, TypeVar

from lib.point import Point
from lib.region import Region

T = TypeVar('T')


@dataclass
class Grid[T]:
    rows: list[list[T]] = field(default_factory=list)

    @property
    def width(self) -> int:
        return len(self.rows[0])

    @property
    def height(self) -> int:
        return len(self.rows)

    def find(self, val: T) -> Optional[Point]:
        return next(self.find_all(val))

    def find_all(self, val: T) -> Generator[Point]:
        for y, row in enumerate(self.rows):
            for x, v in enumerate(row):
                if v == val:
                    yield Point(x, y)

    def at(self, p: Point) -> T:
        return self.rows[p.y][p.x]

    def set(self, p: Point, val: T) -> None:
        self.rows[p.y][p.x] = val

    def in_bounds(self, p: Point) -> bool:
        return (0 <= p.y < self.height) and (0 <= p.x < self.width)

    def column(self, x: int) -> list[T]:
        return [r[x] for r in self.rows]

    def neighbors(self, p: Point) -> list[Point]:
        ret = []
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n = Point(p.x + dx, p.y + dy)
            if self.in_bounds(n):
                ret.append(n)
        return ret

    def items(self) -> Generator[Tuple[Point, T]]:
        for y, row in enumerate(self.rows):
            for x, val in enumerate(row):
                yield Point(x, y), val

    def flood(self, start: Point) -> Region:
        value = self.at(start)
        queue = [start]
        points: set[Point] = set()
        seen: set[Point] = set()

        while queue:
            p = queue.pop(0)
            seen.add(p)

            if self.at(p) != value:
                continue

            points.add(p)

            for np in self.neighbors(p):
                if np not in seen:
                    queue.append(np)

        return Region(points=points)
