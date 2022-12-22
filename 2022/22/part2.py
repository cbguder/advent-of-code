#!/usr/bin/env python3

import re

# I'm sure there's a better way to do this
RELS = {
    (0, 1): {
        2: ((2, 0), 2),
        3: ((3, 0), 1),
    },
    (0, 2): {
        0: ((2, 1), 2),
        1: ((1, 1), 1),
        3: ((3, 0), 0),
    },
    (1, 1): {
        0: ((0, 2), 3),
        2: ((2, 0), 3),
    },
    (2, 0): {
        2: ((0, 1), 2),
        3: ((1, 1), 1),
    },
    (2, 1): {
        0: ((0, 2), 2),
        1: ((3, 0), 1),
    },
    (3, 0): {
        0: ((2, 1), 3),
        1: ((0, 2), 0),
        2: ((0, 1), 3),
    },
}


def block(x, y):
    return (x // 50), (y // 50)


def move(pos, facing):
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

    dest_bl = block(new_x, new_y)
    if dest_bl in RELS:
        return new_x, new_y, facing

    src_bl = block(*pos)
    dest_bl, rot = RELS[src_bl][facing]

    x_in_bl = new_x % 50
    y_in_bl = new_y % 50
    pos_before_rot = (x_in_bl, y_in_bl)

    if rot == 1:
        x_in_bl, y_in_bl = (y_in_bl, 49 - x_in_bl)
    elif rot == 2:
        x_in_bl, y_in_bl = (49 - x_in_bl, 49 - y_in_bl)
    elif rot == 3:
        x_in_bl, y_in_bl = (49 - y_in_bl, x_in_bl)

    new_facing = (facing + rot) % 4

    new_x = dest_bl[0] * 50 + x_in_bl
    new_y = dest_bl[1] * 50 + y_in_bl

    return new_x, new_y, new_facing


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
                new_x, new_y, new_facing = move(pos, facing)

                if grid[new_x][new_y] == "#":
                    break
                else:
                    assert grid[new_x][new_y] == "."
                    pos = (new_x, new_y)
                    facing = new_facing

    pwd = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing
    print(pwd)


if __name__ == "__main__":
    main()
