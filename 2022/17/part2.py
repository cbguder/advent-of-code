#!/usr/bin/env python3


def add_shape(grid, idx):
    grid["shape_y"] = len(grid["rows"]) + 3

    if idx == 0:
        grid["shape"] = [
            0b0011110
        ]
    elif idx == 1:
        grid["shape"] = [
            0b0001000,
            0b0011100,
            0b0001000
        ]
    elif idx == 2:
        grid["shape"] = [
            0b0011100,
            0b0000100,
            0b0000100
        ]
    elif idx == 3:
        grid["shape"] = [
            0b0010000,
            0b0010000,
            0b0010000,
            0b0010000
        ]
    elif idx == 4:
        grid["shape"] = [
            0b0011000,
            0b0011000
        ]


def move_shape(grid, move):
    new_shape = []

    cant_move = False
    shape_y = grid["shape_y"]

    for i, row in enumerate(grid["shape"]):
        if move == ">":
            cant_move = (row % 2) == 1
            new_row = row >> 1
        elif move == "<":
            cant_move = (row & 0b1000000) != 0
            new_row = (row << 1) & 0b1111111

        if not cant_move:
            dest_row = get_row(grid, shape_y + i)
            cant_move = (dest_row & new_row) != 0

        if cant_move:
            return

        new_shape.append(new_row)

    grid["shape"] = new_shape


def get_row(grid, i):
    assert i >= 0
    if len(grid["rows"]) > i:
        return grid["rows"][i]
    return 0


def move_shape_down(grid):
    shape_y = grid["shape_y"]
    should_settle = shape_y == 0

    if not should_settle:
        for i, row in enumerate(grid["shape"]):
            dest_row = get_row(grid, shape_y + i - 1)
            should_settle = (dest_row & row) > 0
            if should_settle:
                break

    if should_settle:
        while len(grid["rows"]) < shape_y + len(grid["shape"]):
            grid["rows"].append(0)

        for i, row in enumerate(grid["shape"]):
            grid["rows"][shape_y + i] |= row
    else:
        grid["shape_y"] -= 1

    return should_settle


def main():
    with open("input") as f:
        moves = f.read().strip()

    grid = {
        "rows": [],
        "shape": None,
    }

    m = 0
    runs = 1000000000000 % 1745
    # sep = 0
    # step = 0

    for i in range(runs):
        # if i % 1745 == 0:
        #     print(i, len(grid["rows"])-step)
        #     step = len(grid["rows"])
        add_shape(grid, i % 5)

        while True:
            move = moves[m]
            m = (m + 1) % len(moves)

            move_shape(grid, move)
            settled = move_shape_down(grid)
            if settled:
                # if grid["rows"][-1] == 0b1111111:
                #     print(i, i-sep)
                #     sep = i
                break

    h = len(grid["rows"])
    h += (1000000000000 // 1745) * 2785
    print(h)


if __name__ == "__main__":
    main()
