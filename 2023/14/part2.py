#!/usr/bin/env python3

import re

CYCLES = 1000000000


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    seen = {
        summ(grid): 0,
    }

    offset = None
    mod = None

    cur = grid[:]
    for i in range(CYCLES):
        cur = rotate(cur)
        m = summ(cur)

        if m in seen:
            offset = seen[m]
            mod = i - offset
            break

        seen[m] = i + 1

    real_cycles = (CYCLES % mod) + offset - 1

    cur = grid[:]
    for i in range(real_cycles):
        cur = rotate(cur)
    print(weight(cur))


def summ(grid):
    return "".join(grid)


def weight(grid):
    ret = 0
    n = len(grid)
    for row in grid:
        ret += n * row.count("O")
        n -= 1
    return ret


def rotate(grid):
    rows = grid[:]

    # rotate north
    cols = transpose(rows)
    for i, col in enumerate(cols):
        cols[i] = shift(col, left=True)
    rows = transpose(cols)

    # rotate west
    for i, row in enumerate(rows):
        rows[i] = shift(row, left=True)

    # rotate south
    cols = transpose(rows)
    for i, col in enumerate(cols):
        cols[i] = shift(col, left=False)
    rows = transpose(cols)

    # rotate east
    for i, row in enumerate(rows):
        rows[i] = shift(row, left=False)

    return rows


def transpose(grid):
    return [
        "".join(row[i] for row in grid)
        for i in range(len(grid[0]))
    ]


def shift(col, left):
    parts = re.split(r"(#+)", col)
    for i, part in enumerate(parts):
        if set(part) != {"#"}:
            shifted = sorted(list(part))
            if left:
                shifted = reversed(shifted)
            parts[i] = "".join(shifted)

    return "".join(parts)


if __name__ == "__main__":
    main()
