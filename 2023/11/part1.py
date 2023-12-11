#!/usr/bin/env python3

from itertools import combinations


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

            if set(line) == {"."}:
                grid.append(line)

    w = len(grid[0])
    cols = []
    for i in range(w):
        col = [row[i] for row in grid]
        cols.append(col)

        if set(col) == {"."}:
            cols.append(col)

    galaxies = []

    w = len(cols)
    h = len(cols[0])
    for i in range(h):
        for j in range(w):
            if cols[j][i] == "#":
                galaxies.append((i, j))

    ret = 0
    for g1, g2 in combinations(galaxies, 2):
        ret += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    print(ret)


if __name__ == "__main__":
    main()
