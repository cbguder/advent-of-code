#!/usr/bin/env python3

from collections import defaultdict


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))

    neighbors = defaultdict(set)

    for node in find_nodes(grid):
        for rstart, rend, d in find_runs(grid, node):
            neighbors[rstart].add((rend, d))
            neighbors[rend].add((rstart, d))

    ret = longest_path(neighbors, start, end)
    print(ret)


def find_nodes(grid):
    h = len(grid)
    w = len(grid[0])

    for i in range(h):
        for j in range(w):
            if grid[i][j] != "#":
                nexts = list(get_next(grid, (i, j)))
                if len(nexts) != 2:
                    yield i, j


def longest_path(neighbors, start, end):
    ret = -1

    queue = [(start, 0, [])]

    while queue:
        cur, d1, seen = queue.pop()
        if cur == end:
            ret = max(ret, d1)

        for next, d2 in neighbors[cur]:
            if next not in seen:
                queue.append((next, d1 + d2, seen + [cur]))

    return ret


def find_runs(grid, node):
    for next in get_next(grid, node):
        run = [node, next]

        while True:
            cur, prev = run[-1], run[-2]
            nexts = set(get_next(grid, cur)) - {prev}

            if len(nexts) == 1:
                next = nexts.pop()
                run.append(next)
            else:
                yield run[0], run[-1], len(run) - 1
                break


def get_next(grid, pos):
    x, y = pos
    h = len(grid)
    w = len(grid[0])

    for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != "#":
            yield nx, ny


if __name__ == "__main__":
    main()
