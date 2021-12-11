#!/usr/bin/env python3


def main():
    grid = []

    with open('input') as f:
        for line in f:
            grid.append(list(map(int, [x for x in line.strip()])))

    i = 1
    while True:
        flashes = step(grid)
        if flashes == 100:
            print(i)
            return
        i += 1


def step(grid):
    to_flash = set()

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            grid[i][j] += 1
            if grid[i][j] > 9:
                to_flash.add((i, j))

    flashed = set()

    while True:
        to_flash_now = to_flash.copy()
        flashed.update(to_flash)
        to_flash.clear()

        if not to_flash_now:
            break

        for pt in set(to_flash_now):
            for np in neighbors(pt):
                grid[np[0]][np[1]] += 1
                if grid[np[0]][np[1]] > 9:
                    if np not in flashed:
                        to_flash.add(np)

    for pt in flashed:
        grid[pt[0]][pt[1]] = 0

    return len(flashed)


def neighbors(pt):
    for x in range(max(pt[0] - 1, 0), min(pt[0] + 2, 10)):
        for y in range(max(pt[1] - 1, 0), min(pt[1] + 2, 10)):
            if pt != (x, y):
                yield x, y


if __name__ == '__main__':
    main()
