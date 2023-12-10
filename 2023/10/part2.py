#!/usr/bin/env python3

from collections import defaultdict


def main():
    grid = []
    start = None
    y = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

            if start is None and "S" in line:
                start = (y, line.index("S"))

            y += 1

    loop = find_loop(grid, start)
    expanded = expand_grid(grid, loop)
    fill_outside(expanded)

    h = len(grid)
    w = len(grid[0])
    ret = 0
    for y in range(h):
        for x in range(w):
            if inside(y, x, expanded):
                ret += 1
    print(ret)


def inside(y, x, expanded):
    for ey in range(y * 3, y * 3 + 3):
        for ex in range(x * 3, x * 3 + 3):
            if expanded[ey][ex] != " ":
                return False
    return True


def expand_grid(grid, loop):
    h = len(grid)
    w = len(grid[0])

    expanded = []
    for y in range(h):
        l1 = []
        l2 = []
        l3 = []

        for x in range(w):
            if (y, x) in loop:
                val = grid[y][x]
                if val == "J":
                    l1 += [" ", "#", " "]
                    l2 += ["#", "#", " "]
                    l3 += [" ", " ", " "]
                elif val == "|":
                    l1 += [" ", "#", " "]
                    l2 += [" ", "#", " "]
                    l3 += [" ", "#", " "]
                elif val == "F":
                    l1 += [" ", " ", " "]
                    l2 += [" ", "#", "#"]
                    l3 += [" ", "#", " "]
                elif val == "L":
                    l1 += [" ", "#", " "]
                    l2 += [" ", "#", "#"]
                    l3 += [" ", " ", " "]
                elif val == "-":
                    l1 += [" ", " ", " "]
                    l2 += ["#", "#", "#"]
                    l3 += [" ", " ", " "]
                elif val == "7":
                    l1 += [" ", " ", " "]
                    l2 += ["#", "#", " "]
                    l3 += [" ", "#", " "]
                elif val == "S":
                    l1 += ["#", "#", "#"]
                    l2 += ["#", "#", "#"]
                    l3 += ["#", "#", "#"]
            else:
                l1 += [" ", " ", " "]
                l2 += [" ", " ", " "]
                l3 += [" ", " ", " "]

        expanded += [l1, l2, l3]

    return expanded


def find_loop(grid, start):
    h = len(grid)
    w = len(grid[0])

    prevs = defaultdict(set)

    queue = [start]
    seen = set()
    while queue:
        y, x = queue.pop(0)
        seen.add((y, x))
        val1 = grid[y][x]

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx

            if 0 <= ny < h and 0 <= nx < w:
                val2 = grid[ny][nx]
                if valid(val1, val2, dx, dy):
                    prevs[(ny, nx)].add((y, x))

                    if (ny, nx) not in seen:
                        queue.append((ny, nx))

    loop = set()
    queue = [start]
    while queue:
        cur = queue.pop(0)
        loop.add(cur)
        for prev in prevs[cur]:
            if prev not in loop:
                queue.append(prev)

    return loop


def fill_outside(grid):
    h = len(grid)
    w = len(grid[0])

    queue = []

    for y in range(h):
        for x in range(w):
            if grid[y][x] == "#":
                break
            queue.append((y, x))
        for x in range(w - 1, 0, -1):
            if grid[y][x] == "#":
                break
            queue.append((y, x))

    for x in range(w):
        for y in range(h):
            if grid[y][x] == "#":
                break
            queue.append((y, x))
        for y in range(h - 1, 0, -1):
            if grid[y][x] == "#":
                break
            queue.append((y, x))

    seen = set()
    while queue:
        y, x = queue.pop(0)
        if (y, x) in seen:
            continue
        grid[y][x] = "O"
        seen.add((y, x))

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if grid[ny][nx] == " ":
                    if (ny, nx) not in seen:
                        queue.append((ny, nx))


def valid(val1, val2, dx, dy):
    if dx == 1:
        return val1 in "-LFS" and val2 in "-J7S"

    if dx == -1:
        return val1 in "-J7S" and val2 in "-LFS"

    if dy == 1:
        return val1 in "|7FS" and val2 in "|JLS"

    if dy == -1:
        return val1 in "|JLS" and val2 in "|7FS"

    return False


if __name__ == "__main__":
    main()
