#!/usr/bin/env python3
import re


def main():
    grid = []
    path = []
    grid_done = False

    with open("input") as f:
        for line in f:
            line = line.strip("\n")

            if line == "":
                grid_done = True
            elif grid_done:
                while line:
                    if line[0] in {"L", "R"}:
                        path.append(line[0])
                        line = line[1:]
                    else:
                        m = re.match(r"\d+", line)
                        val = m.group(0)
                        path.append(int(val))
                        line = line[len(val):]
            else:
                grid.append([c for c in line])

    x_ranges = []
    y_ranges = []
    width = 0

    for row in grid:
        min_y = float("inf")
        max_y = 0
        for i, c in enumerate(row):
            if c != " ":
                min_y = min(min_y, i)
                max_y = max(max_y, i)

        y_ranges.append((min_y, max_y))
        width = max(width, len(row))

    for y in range(width):
        min_x = float("inf")
        max_x = 0
        for x in range(len(grid)):
            c = " "
            if len(grid[x]) > y:
                c = grid[x][y]
            if c != " ":
                min_x = min(min_x, x)
                max_x = max(max_x, x)
        x_ranges.append((min_x, max_x))

    facing = 0
    pos = None
    for i, c in enumerate(grid[0]):
        if c == ".":
            pos = (0, i)
            break

    for step in path:
        if step == "L":
            facing = (facing - 1) % 4
        elif step == "R":
            facing = (facing + 1) % 4
        else:
            for _ in range(step):
                new_x, new_y = pos

                if facing == 0:
                    new_y += 1
                elif facing == 1:
                    new_x += 1
                elif facing == 2:
                    new_y -= 1
                elif facing == 3:
                    new_x -= 1
                else:
                    assert False

                if facing in {0, 2}:
                    min_y, max_y = y_ranges[new_x]
                    if new_y < min_y:
                        new_y = max_y
                    elif new_y > max_y:
                        new_y = min_y
                else:
                    min_x, max_x = x_ranges[new_y]
                    if new_x < min_x:
                        new_x = max_x
                    elif new_x > max_x:
                        new_x = min_x

                if grid[new_x][new_y] == "#":
                    break
                else:
                    assert grid[new_x][new_y] == "."
                    pos = (new_x, new_y)

    pwd = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing
    print(pwd)


if __name__ == "__main__":
    main()
