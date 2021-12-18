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

    res = find_valid_velocities(target)
    print(res)


def find_valid_velocities(area):
    vx_max = area.max.x
    vy_min = area.min.y
    vy_max = int(abs(area.min.y))

    valid_velocities = 0

    for vx in range(vx_max + 1):
        for vy in range(vy_min, vy_max + 1):
            v = Velocity(vx, vy)
            if is_valid_velocity(v, area):
                valid_velocities += 1

    return valid_velocities


def is_valid_velocity(v, area):
    pt = Point(0, 0)
    highest = 0

    while True:
        pt, v = step(pt, v)
        if pt.y > highest:
            highest = pt.y

        if area.contains(pt):
            return True

        if area.missed(pt):
            return False


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
