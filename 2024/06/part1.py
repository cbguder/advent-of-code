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
    locs = {p}
    d = (-1, 0)

    while True:
        np = (p[0] + d[0], p[1] + d[1])

        if np[0] < 0 or np[1] < 0 or np[0] >= h or np[1] >= w:
            break

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

        locs.add(np)
        p = np

    print(len(locs))


if __name__ == "__main__":
    main()
