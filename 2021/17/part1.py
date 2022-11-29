#!/usr/bin/env python3

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class Velocity:
    x: int
    y: int


@dataclass(frozen=True)
class Area:
    min: Point
    max: Point

    def contains(self, pt):
        return (self.min.x <= pt.x <= self.max.x) and (self.min.y <= pt.y <= self.max.y)

    def missed(self, pt):
        return pt.x > self.max.x or pt.y < self.min.y

    def height(self):
        return int(abs(self.max.y - self.min.y))


def main():
    with open("input") as f:
        input = f.readline()

    match = re.match(r"target area: x=(.+)\.\.(.+), y=(.+)\.\.(.+)", input)
    xmin, xmax, ymin, ymax = tuple(map(int, match.group(1, 2, 3, 4)))

    assert xmin > 0
    assert xmax > 0
    assert ymin < 0
    assert ymax < 0
    assert xmin < xmax
    assert ymin < ymax

    target = Area(Point(xmin, ymin), Point(xmax, ymax))

    res = find_highest_y(target)
    print(res)


def find_highest_y(area):
    vx_max = area.max.x
    vy_max = int(abs(area.min.y))

    highest_overall = 0

    for vx in range(vx_max + 1):
        for vy in range(vy_max + 1):
            v = Velocity(vx, vy)
            highest_y = find_highest_y_with_velocity(v, area)
            if highest_y is not None and highest_y > highest_overall:
                highest_overall = highest_y

    return highest_overall


def find_highest_y_with_velocity(v, area):
    pt = Point(0, 0)
    highest = 0

    while True:
        pt, v = step(pt, v)
        if pt.y > highest:
            highest = pt.y

        if area.contains(pt):
            break

        if area.missed(pt):
            return None

    return highest


def step(pt, v):
    x = pt.x + v.x
    y = pt.y + v.y

    vx = v.x
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1

    vy = v.y - 1

    return Point(x, y), Velocity(vx, vy)


if __name__ == '__main__':
    main()
