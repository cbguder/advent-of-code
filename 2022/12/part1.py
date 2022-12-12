#!/usr/bin/env python3


def find_nexts(grid, start):
    a = grid[start[0]][start[1]]

    for x in {start[0] - 1, start[0] + 1}:
        if x < 0 or x >= len(grid):
            continue
        pt = (x, start[1])
        b = grid[pt[0]][pt[1]]
        if ord(b) - ord(a) <= 1:
            yield pt

    for y in {start[1] - 1, start[1] + 1}:
        if y < 0 or y >= len(grid[0]):
            continue
        pt = (start[0], y)
        b = grid[pt[0]][pt[1]]
        if ord(b) - ord(a) <= 1:
            yield pt


def main():
    grid = []
    best = []
    pos = None
    dest = None

    with open("input") as f:
        x = 0

        for line in f:
            line = line.strip()
            cells = [x for x in line]
            for i, cell in enumerate(cells):
                if cell == "S":
                    cells[i] = "a"
                    pos = (x, i)
                elif cell == "E":
                    cells[i] = "z"
                    dest = (x, i)
            grid.append(cells)
            best.append([None] * len(cells))
            x += 1

    best[pos[0]][pos[1]] = 0

    stack = [pos]
    while True:
        if len(stack) == 0:
            break

        start = stack.pop()
        start_best = best[start[0]][start[1]]

        for next in find_nexts(grid, start):
            cur_best = best[next[0]][next[1]]
            if cur_best is None or cur_best > start_best + 1:
                best[next[0]][next[1]] = start_best + 1
                stack.append(next)

    print(best[dest[0]][dest[1]])


if __name__ == "__main__":
    main()
