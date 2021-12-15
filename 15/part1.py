#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def main():
    raw_risks = []

    with open('input') as f:
        for line in f:
            row = list(map(int, [x for x in line.strip()]))
            raw_risks.append(row)

    w = len(raw_risks[0])
    h = len(raw_risks)

    risks = {}
    for y, row in enumerate(raw_risks):
        for x, risk in enumerate(row):
            pt = Point(x, y)
            risks[pt] = risk

    print(solve(risks, w, h))


def solve(risks, w, h):
    orig = Point(0, 0)
    prev = {
        orig: 0
    }

    queue = [orig]

    while queue:
        pt = queue.pop(0)
        for np in neighbors(pt, w, h):
            total_risk = prev[pt] + risks[np]
            if np not in prev or prev[np] > total_risk:
                prev[np] = total_risk
                queue.append(np)

    dst = Point(w - 1, h - 1)
    return prev[dst]


def neighbors(pt, w, h):
    ret = []

    if pt.x > 0:
        ret.append(Point(pt.x - 1, pt.y))
    if pt.x < w - 1:
        ret.append(Point(pt.x + 1, pt.y))
    if pt.y > 0:
        ret.append(Point(pt.x, pt.y - 1))
    if pt.y < h - 1:
        ret.append(Point(pt.x, pt.y + 1))

    return ret


if __name__ == '__main__':
    main()
