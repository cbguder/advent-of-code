#!/usr/bin/env python3

from collections import defaultdict


def main():
    grid = []
    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    w = len(grid[0])
    h = len(grid)

    to_visit = set()
    for y in range(h):
        for x in range(w):
            to_visit.add((y, x))

    ret = 0

    while to_visit:
        p = to_visit.pop()
        val, pts = flood(p, grid)

        to_visit.difference_update(pts)
        ret += cost(pts)

    print(ret)


def flood(p, grid):
    val = at(p, grid)
    ret = {p}
    seen = set()
    to_visit = [p]

    while to_visit:
        c = to_visit.pop(0)
        if c in seen:
            continue

        seen.add(c)

        if at(c, grid) == val:
            ret.add(c)

            for np in neighbors(c, grid):
                to_visit.append(np)

    return val, ret


def cost(pts):
    ys = [p[0] for p in pts]
    xs = [p[1] for p in pts]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    edges = 0

    for y in range(min_y, max_y + 1):
        for x in range(min_x - 1, max_x + 1):
            p1, p2 = (y, x), (y, x + 1)
            if (p1 in pts) != (p2 in pts):
                edges += 1

    for x in range(min_x, max_x + 1):
        for y in range(min_y - 1, max_y + 1):
            p1, p2 = (y, x), (y + 1, x)
            if (p1 in pts) != (p2 in pts):
                edges += 1

    return edges * len(pts)


def at(p, grid):
    y, x = p
    return grid[y][x]


def neighbors(p, grid):
    w = len(grid[0])
    h = len(grid)

    py, px = p
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        y, x = py + dy, px + dx
        if 0 <= y < h and 0 <= x < w:
            yield y, x


if __name__ == "__main__":
    main()
