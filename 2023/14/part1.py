#!/usr/bin/env python3
import re


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    cols = []
    for i in range(len(grid[0])):
        col = "".join(row[i] for row in grid)
        cols.append(col)

    ret = 0
    for col in cols:
        s = shift(col)
        ret += weight(s)
    print(ret)


def weight(col):
    ret = 0
    n = len(col)
    for c in col:
        if c == "O":
            ret += n
        n -= 1
    return ret


def shift(col):
    parts = re.split(r"(#+)", col)
    for i, part in enumerate(parts):
        if set(part) != {"#"}:
            parts[i] = "".join(reversed(sorted(list(part))))

    return "".join(parts)


if __name__ == "__main__":
    main()
