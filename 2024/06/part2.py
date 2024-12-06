#!/usr/bin/env python3


def main():
    grid = []
    p = None

    y = 0
    with open("input") as f:
        for line in f:
            line = line.strip()
            row = [c for c in line]

            if p is None:
                if "^" in row:
                    x = row.index("^")
                    p = (y, x)

            grid.append(row)
            y += 1

    w = len(grid[0])
    h = len(grid)

    ret = 0

    for y in range(h):
        for x in range(w):
            if grid[y][x] == ".":
                new_grid = [r[:] for r in grid]
                new_grid[y][x] = "#"
                if is_loop(p, new_grid):
                    ret += 1

    print(ret)


def is_loop(p, grid):
    w = len(grid[0])
    h = len(grid)
    d = (-1, 0)
    locs = {(p, d)}

    while True:
        np = (p[0] + d[0], p[1] + d[1])

        if np[0] < 0 or np[1] < 0 or np[0] >= h or np[1] >= w:
            return False

        if grid[np[0]][np[1]] == "#":
            if d == (-1, 0):
                d = (0, 1)
            elif d == (0, 1):
                d = (1, 0)
            elif d == (1, 0):
                d = (0, -1)
            else:
                d = (-1, 0)
            continue

        if (np, d) in locs:
            return True

        locs.add((np, d))
        p = np


if __name__ == "__main__":
    main()
