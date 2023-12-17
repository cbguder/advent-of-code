#!/usr/bin/env python3

from bisect import insort_left


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            nums = list(map(int, [c for c in line]))
            grid.append(nums)

    ret = solve(grid)
    print(ret)


def solve(grid):
    h = len(grid)
    w = len(grid[0])

    queue = [
        (0, 1, (0, 1), (0, 1)),
        (0, 1, (1, 0), (1, 0)),
    ]

    memo = {}

    while queue:
        tot, n, pos, dir = queue.pop(0)
        y, x = pos
        dy, dx = dir

        if y < 0 or y >= h or x < 0 or x >= w:
            continue

        if n > 3:
            continue

        key = (n, pos, dir)
        if key in memo:
            continue

        tot += grid[y][x]
        if y == h - 1 and x == w - 1:
            return tot

        if memo.get(key, float("inf")) > tot:
            memo[key] = tot
            insort_left(queue, (tot, n + 1, (y + dy, x + dx), dir))
            insort_left(queue, (tot, 1, (y + dx, x + dy), (dx, dy)))
            insort_left(queue, (tot, 1, (y - dx, x - dy), (-dx, -dy)))

    return None


if __name__ == "__main__":
    main()
