#!/usr/bin/env python3


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    start = find_start(grid)

    pos = {start}
    for i in range(64):
        new_pos = set()
        for x, y in pos:
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                    if grid[x + dx][y + dy] != "#":
                        new_pos.add((x + dx, y + dy))
        pos = new_pos

    print(len(pos))


def find_start(grid):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "S":
                return (i, j)


if __name__ == "__main__":
    main()
