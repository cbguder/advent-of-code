#!/usr/bin/env python3

from itertools import combinations

MIN = 200000000000000
MAX = 400000000000000


def main():
    points = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split(" @ ")
            p, v = (tuple(map(int, p.split(","))) for p in parts)
            points.append((p, v))

    ret = 0
    for pt1, pt2 in combinations(points, 2):
        if intersects(pt1, pt2):
            ret += 1
    print(ret)


def intersects(pt1, pt2):
    p1, v1 = pt1
    p2, v2 = pt2

    v1y_norm = v1[1] / v1[0]
    v2y_norm = v2[1] / v2[0]

    ystep = v2y_norm - v1y_norm
    if ystep == 0:
        return False

    p2_ = move(pt2, p1[0])
    ydiff = p1[1] - p2_[1]
    t = ydiff / ystep

    new_x = p1[0] + t
    new_y = p1[1] + v1y_norm * t

    t1 = (new_x - p1[0]) / v1[0]
    t2 = (new_x - p2[0]) / v2[0]
    if t1 < 0 or t2 < 0:
        return False

    collides = MIN <= new_x <= MAX and MIN <= new_y <= MAX
    return collides


def move(pt, new_x):
    p, v = pt
    dist = new_x - p[0]
    t = dist / v[0]
    new_y = p[1] + v[1] * t
    return new_x, new_y


if __name__ == "__main__":
    main()
