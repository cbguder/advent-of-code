#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappop, heappush

import pyperclip

from lib.grid import Grid
from lib.point import Point


def main():
    rows = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            rows.append([c for c in line])

    grid = Grid(rows)
    start = grid.find("S")
    end = grid.find("E")

    ret = solve(grid, start, end)

    print(ret)
    pyperclip.copy(ret)


DIRS = [Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1)]


def solve(grid, start, end):
    dist = {start: 0}
    prev = defaultdict(set)
    pq = [(0, start, 0)]

    while pq:
        dst, p, d = heappop(pq)

        d1 = (d + 1) % 4
        d2 = (d - 1) % 4

        nexts = [
            (p + DIRS[d], d, dst + 1),
            (p + DIRS[d1], d1, dst + 1001),
            (p + DIRS[d2], d2, dst + 1001),
        ]

        for n, dir_to_n, new_dst in nexts:
            if grid.at(n) == "#":
                continue

            if new_dst <= dist.get((n, dir_to_n), float("inf")):
                dist[(n, dir_to_n)] = new_dst
                prev[(n, dir_to_n)].add((p, d))
                heappush(pq, (new_dst, n, dir_to_n))

    min_dst = min(dist.get((end, i), float("inf")) for i in range(4))
    queue = [(end, i) for i in range(4) if dist.get((end, i)) == min_dst]
    pts = set()
    while queue:
        p, d = queue.pop(0)
        pts.add(p)
        queue += prev[(p, d)]

    return len(pts)


if __name__ == "__main__":
    main()
