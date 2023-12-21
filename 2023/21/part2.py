#!/usr/bin/env python3


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    start = find_start(grid)
    h = len(grid)
    w = len(grid[0])

    pos = {start}

    # 26501365 = 131 * 202300 + 65
    for i in range(65 + 131 * 2 + 1):
        if i % 131 == 65:
            n = len(pos)
            g = guess(1 + ((i - 65) // 131))
            print(i, n, g - n)
        new_pos = set()
        for x, y in pos:
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx = x + dx
                ny = y + dy
                if grid[nx % h][ny % w] != "#":
                    new_pos.add((nx, ny))
        pos = new_pos


# Fit using Wolfram Alpha
def guess(x):
    return (14881 * x * x) - (14821 * x) + 3682


def find_start(grid):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "S":
                return (i, j)


if __name__ == "__main__":
    main()
