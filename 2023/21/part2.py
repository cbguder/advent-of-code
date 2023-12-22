#!/usr/bin/env python3

from collections import defaultdict


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    # print_runs(grid)     # Shows the quadratic growth when graphed
    # check_loops(grid)    # Shows 131x131 grids starting to loop after 131 steps
    # check_guesses(grid)  # Confirms the fit function is correct

    # 26501365 = 131 * 202300 + 65
    print(guess(202300 + 1))


def print_runs(grid):
    start = find_start(grid)
    h = len(grid)
    w = len(grid[0])

    pos = {start}

    for i in range(500):
        print(f"{i},{len(pos)}")
        new_pos = set()
        for x, y in pos:
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx = x + dx
                ny = y + dy
                if grid[nx % h][ny % w] != "#":
                    new_pos.add((nx, ny))
        pos = new_pos


def check_guesses(grid):
    start = find_start(grid)
    h = len(grid)
    w = len(grid[0])

    pos = {start}

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


def check_loops(grid):
    start = find_start(grid)
    h = len(grid)
    w = len(grid[0])

    pos = {
        (0, 0): {start}
    }

    first_seen = {}
    last_seen = {}

    for i in range(600):
        new_pos = defaultdict(set)

        for (gx, gy), gpos in pos.items():
            if (gx, gy) not in first_seen:
                first_seen[(gx, gy)] = i
            if len(gpos) == 7407:
                if (gx, gy) not in last_seen:
                    last_seen[(gx, gy)] = i
                    print((gx, gy), "completed loop", first_seen[(gx, gy)], i, i - first_seen[(gx, gy)])

            interns, externs = step(grid, gpos)
            new_pos[(gx, gy)] = interns
            for (x, y) in externs:
                pgx, pgy = gx, gy
                if x < 0:
                    pgx -= 1
                elif x >= h:
                    pgx += 1
                if y < 0:
                    pgy -= 1
                elif y >= w:
                    pgy += 1

                new_pos[(pgx, pgy)].add((x % h, y % w))

        pos = new_pos


def step(grid, pos):
    h = len(grid)
    w = len(grid[0])

    interns = set()
    externs = set()

    for x, y in pos:
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx = x + dx
            ny = y + dy
            if grid[nx % h][ny % w] != "#":
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    externs.add((nx, ny))
                else:
                    interns.add((nx, ny))

    return interns, externs


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
