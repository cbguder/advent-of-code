#!/usr/bin/env python3


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    ret = longest_path(grid)
    print(ret)


def longest_path(grid):
    start = (0, grid[0].index("."))
    dist = {
        start: 0,
    }
    queue = [
        (start,)
    ]

    while queue:
        path = queue.pop(0)

        pos = path[-1]
        next_dist = dist[pos] + 1

        for next_pos in get_next(grid, pos):
            if next_pos not in path:
                dist[next_pos] = max(dist.get(next_pos, 0), next_dist)
                queue.append(path + (next_pos,))

    end = (len(grid) - 1, grid[-1].index("."))
    return dist[end]


def get_next(grid, pos):
    x, y = pos
    h = len(grid)
    w = len(grid[0])

    if grid[x][y] == ">":
        possible_dirs = [(0, 1)]
    elif grid[x][y] == "<":
        possible_dirs = [(0, -1)]
    elif grid[x][y] == "v":
        possible_dirs = [(1, 0)]
    elif grid[x][y] == "^":
        possible_dirs = [(-1, 0)]
    else:
        possible_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for (dx, dy) in possible_dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != "#":
            yield nx, ny


if __name__ == "__main__":
    main()
