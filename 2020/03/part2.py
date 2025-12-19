#!/usr/bin/env python3


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    ret = 1
    for slope in slopes:
        ret *= solve(grid, *slope)
    print(ret)


def solve(grid, dx, dy):
    y, x = 0, 0
    h = len(grid)
    w = len(grid[0])
    trees = 0

    while y < h:
        if grid[y][x] == "#":
            trees += 1
        x = (x + dx) % w
        y += dy

    return trees


if __name__ == "__main__":
    main()
