#!/usr/bin/env python3

from itertools import pairwise


def main():
    pos = (0, 0)
    pts = [pos]

    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split()
            dr, dist, _ = parts
            dist = int(dist)

            pos = add(pos, dr, dist)
            pts.append(pos)

            min_x = min(min_x, pos[1])
            max_x = max(max_x, pos[1])
            min_y = min(min_y, pos[0])
            max_y = max(max_y, pos[0])

    w = max_x - min_x + 1
    h = max_y - min_y + 1

    grid = []
    for _ in range(h):
        grid.append(["."] * w)

    for p1, p2 in pairwise(pts):
        if p1[0] == p2[0]:
            y = p1[0] - min_y
            for x in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                x -= min_x
                grid[y][x] = "#"
        elif p1[1] == p2[1]:
            x = p1[1] - min_x
            for y in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                y -= min_y
                grid[y][x] = "#"
        else:
            assert False

    fill_outside(grid)

    ret = 0
    for row in grid:
        ret += len([x for x in row if x != "O"])
    print(ret)


def fill_outside(grid):
    h = len(grid)
    w = len(grid[0])

    queue = []

    for y in range(h):
        for x in range(w):
            if grid[y][x] == "#":
                break
            queue.append((y, x))
        for x in range(w - 1, 0, -1):
            if grid[y][x] == "#":
                break
            queue.append((y, x))

    for x in range(w):
        for y in range(h):
            if grid[y][x] == "#":
                break
            queue.append((y, x))
        for y in range(h - 1, 0, -1):
            if grid[y][x] == "#":
                break
            queue.append((y, x))

    seen = set()
    while queue:
        y, x = queue.pop(0)
        if (y, x) in seen:
            continue
        grid[y][x] = "O"
        seen.add((y, x))

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if grid[ny][nx] != "#":
                    if (ny, nx) not in seen:
                        queue.append((ny, nx))


def add(pos, dr, dist):
    y, x = pos

    if dr == "R":
        return (y, x + dist)
    elif dr == "L":
        return (y, x - dist)
    elif dr == "U":
        return (y - dist, x)
    elif dr == "D":
        return (y + dist, x)

    assert False


if __name__ == "__main__":
    main()
