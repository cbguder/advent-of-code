#!/usr/bin/env python3

from itertools import combinations

SPACE = 1000000


def main():
    galaxies = []
    empty_cols = []
    empty_rows = []
    grid = []

    with open("input") as f:
        i = 0
        for line in f:
            line = line.strip()
            grid.append(line)

            if set(line) == {"."}:
                empty_rows.append(i)
            else:
                for j, char in enumerate(line):
                    if char == "#":
                        galaxies.append((i, j))
            i += 1

    for i in range(len(grid[0])):
        col = [row[i] for row in grid]
        if set(col) == {"."}:
            empty_cols.append(i)

    for i, galaxy in enumerate(galaxies):
        dx = (SPACE - 1) * len([row for row in empty_rows if row < galaxy[0]])
        dy = (SPACE - 1) * len([col for col in empty_cols if col < galaxy[1]])
        galaxies[i] = (galaxy[0] + dx, galaxy[1] + dy)

    ret = 0
    for g1, g2 in combinations(galaxies, 2):
        ret += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    print(ret)


if __name__ == "__main__":
    main()
