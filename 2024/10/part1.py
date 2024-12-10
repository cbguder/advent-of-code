#!/usr/bin/env python3


def main():
    grid = []

    with open("input") as f:
        for line in f:
            row = [int(c) for c in line.strip()]
            grid.append(row)

    ret = 0
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if line[x] == 0:
                ret += score(grid, (y, x))

    print(ret)


def score(grid, th):
    pos = {th}
    ends = set()

    while pos:
        new_pos = set()
        for p in pos:
            new_pos.update(extend(grid, p))
        for (y, x) in new_pos:
            if grid[y][x] == 9:
                ends.add((y, x))
        pos = new_pos

    return len(ends)


def extend(grid, pos):
    w = len(grid[0])
    h = len(grid)

    ly, lx = pos
    val = grid[ly][lx]

    new_pos = set()

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        y, x = ly + dy, lx + dx
        if 0 <= y < h and 0 <= x < w:
            if grid[y][x] == val + 1:
                new_pos.add((y, x))

    return new_pos


if __name__ == "__main__":
    main()
