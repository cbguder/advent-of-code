#!/usr/bin/env python3


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            grid.append(line)

    ret = 0
    h = len(grid)
    w = len(grid[0])
    for x in range(w):
        ret = max(ret, solve(grid, (0, x, 1, 0)))
        ret = max(ret, solve(grid, (h - 1, x, -1, 0)))
    for y in range(h):
        ret = max(ret, solve(grid, (y, 0, 0, 1)))
        ret = max(ret, solve(grid, (y, w - 1, 0, -1)))

    print(ret)


def solve(grid, start):
    energized = set()
    seen = set()
    beams = {start}

    while True:
        if not beams:
            break

        new_beams = set()

        for y, x, dy, dx in beams:
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
                continue

            if (y, x, dy, dx) in seen:
                continue

            seen.add((y, x, dy, dx))
            energized.add((y, x))
            cell = grid[y][x]

            if cell == "|":
                if dx != 0:
                    new_beams.add((y - 1, x, -1, 0))
                    new_beams.add((y + 1, x, 1, 0))
                else:
                    new_beams.add((y + dy, x + dx, dy, dx))
            elif cell == "-":
                if dy != 0:
                    new_beams.add((y, x - 1, 0, -1))
                    new_beams.add((y, x + 1, 0, 1))
                else:
                    new_beams.add((y + dy, x + dx, dy, dx))
            else:
                if cell == "\\":
                    dy, dx = dx, dy
                elif cell == "/":
                    dy, dx = -dx, -dy

                new_beams.add((y + dy, x + dx, dy, dx))

        beams = new_beams

    return len(energized)


if __name__ == "__main__":
    main()
