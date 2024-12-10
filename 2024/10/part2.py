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
    trails = {(th,)}
    done_trails = set()

    while trails:
        t = trails.pop()
        ly, lx = t[-1]
        if grid[ly][lx] == 9:
            done_trails.add(t)
        else:
            trails.update(extend(grid, t))

    return len(done_trails)


def extend(grid, trail):
    w = len(grid[0])
    h = len(grid)

    ly, lx = trail[-1]
    val = grid[ly][lx]

    new_trails = set()

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        y, x = ly + dy, lx + dx
        if 0 <= y < h and 0 <= x < w:
            if grid[y][x] == val + 1:
                new_trails.add(trail + ((y, x),))

    return new_trails


if __name__ == "__main__":
    main()
