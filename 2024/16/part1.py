#!/usr/bin/env python3

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

    ret = solve(grid, start, end, Point(1, 0))

    print(ret)
    pyperclip.copy(ret)


def solve(grid, start, end, d):
    dist = {start: 0}
    pq = [(0, start, d)]

    seen = set()

    while pq:
        dst, pt, dr = heappop(pq)
        if (pt, dr) in seen:
            continue

        seen.add((pt, dr))

        for n in grid.neighbors(pt):
            if grid.at(n) == "#":
                continue

            dir_to_n = n - pt

            nd = dst + 1
            if dr != dir_to_n:
                nd += 1000

            if n not in dist or dist[n] > nd:
                dist[n] = nd
                heappush(pq, (nd, n, dir_to_n))

    return dist[end]


if __name__ == "__main__":
    main()
