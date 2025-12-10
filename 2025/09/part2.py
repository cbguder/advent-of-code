#!/usr/bin/env python3

import itertools
from functools import cache

import pyperclip
from lib.file import File
from lib.point import Point

points: list[Point] = []


def main():
    global points
    ret = 0

    with open("input") as f:
        ff = File(f)
        real_points = ff.read_points()

    xs = sorted(set(p.x for p in real_points))
    ys = sorted(set(p.y for p in real_points))

    points = [Point(xs.index(p.x), ys.index(p.y)) for p in real_points]

    for a, b in itertools.combinations(points, 2):
        pa = Point(xs[a.x], ys[a.y])
        pb = Point(xs[b.x], ys[b.y])

        d = abs(pa - pb)
        area = (d.x + 1) * (d.y + 1)

        if area > ret:
            if valid_rect(a, b):
                ret = area

    print(ret)
    pyperclip.copy(ret)


def valid_rect(a, b):
    xmin, xmax = min(a.x, b.x), max(a.x, b.x)
    ymin, ymax = min(a.y, b.y), max(a.y, b.y)

    for i in range(xmin, xmax + 1):
        for j in range(ymin, ymax + 1):
            p = Point(i, j)
            if not is_inside(p):
                return False

    return True


def is_on_edge(p, a, b) -> bool:
    if a.x == b.x == p.x:
        return min(a.y, b.y) <= p.y <= max(a.y, b.y)

    if a.y == b.y == p.y:
        return min(a.x, b.x) <= p.x <= max(a.x, b.x)

    return False


@cache
def is_inside(p) -> bool:
    global points
    n = len(points)

    for i in range(n):
        a = points[i]
        b = points[(i + 1) % n]
        if is_on_edge(p, a, b):
            return True

    inside = False
    for i in range(n):
        a = points[i]
        b = points[(i + 1) % n]

        if (a.y > p.y) != (b.y > p.y):
            xinters = a.x + (b.x - a.x) * (p.y - a.y) / (b.y - a.y)
            if p.x < xinters:
                inside = not inside

    return inside


if __name__ == "__main__":
    main()
