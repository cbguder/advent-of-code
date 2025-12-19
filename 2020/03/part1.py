#!/usr/bin/env python3


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    y, x = 0, 0
    h = len(grid)
    w = len(grid[0])
    trees = 0

    while y < h:
        if grid[y][x] == "#":
            trees += 1
        x = (x + 3) % w
        y += 1

    print(trees)


if __name__ == "__main__":
    main()
