#!/usr/bin/env python3


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

    h = len(grid)
    w = len(grid[0])

    dists = []
    for _ in range(h):
        dists.append([None for _ in range(w)])

    dists[start[0]][start[1]] = 0

    maxdist = 0

    queue = [start]
    seen = set()
    while queue:
        y, x = queue.pop(0)
        seen.add((y, x))
        dist = dists[y][x]

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx

            if (ny, nx) in seen:
                continue

            if 0 <= ny < h and 0 <= nx < w:
                val = grid[ny][nx]
                if valid(val, dx, dy):
                    maxdist = max(maxdist, dist + 1)
                    dists[ny][nx] = dist + 1
                    queue.append((ny, nx))

    print(maxdist)


def valid(val, dx, dy):
    if dx == 1:
        return val in "-J7"

    if dx == -1:
        return val in "-LF"

    if dy == 1:
        return val in "|JL"

    if dy == -1:
        return val in "|7F"

    return False


if __name__ == "__main__":
    main()
