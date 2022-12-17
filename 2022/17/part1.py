#!/usr/bin/env python3


def add_shape(grid, idx):
    assert not grid["shape"]
    y = grid["height"] + 3

    if idx == 0:
        shape = {
            (2, y), (3, y), (4, y), (5, y),
        }
    elif idx == 1:
        shape = {
            (3, y + 2),
            (2, y + 1), (3, y + 1), (4, y + 1),
            (3, y + 0),
        }
    elif idx == 2:
        shape = {
            (4, y + 2),
            (4, y + 1),
            (2, y + 0), (3, y + 0), (4, y + 0),
        }
    elif idx == 3:
        shape = {
            (2, y + 3),
            (2, y + 2),
            (2, y + 1),
            (2, y + 0),
        }
    elif idx == 4:
        shape = {
            (2, y + 1), (3, y + 1),
            (2, y + 0), (3, y + 0),
        }
    else:
        assert False

    grid["shape"] = shape


def move_shape(grid, move):
    new_shape = set()

    for point in grid["shape"]:
        if move == ">":
            new_point = (point[0]+1, point[1])
        elif move == "<":
            new_point = (point[0]-1, point[1])
        else:
            assert False

        cant_move = new_point[0] == -1 or new_point[0] == 7 or new_point in grid["settled"]
        if cant_move:
            return

        new_shape.add(new_point)

    grid["shape"] = new_shape


def move_shape_down(grid):
    new_shape = set()

    for point in grid["shape"]:
        new_point = (point[0], point[1] - 1)

        should_settle = new_point[1] == -1 or new_point in grid["settled"]
        if should_settle:
            grid["settled"].update(grid["shape"])
            grid["height"] = max(p[1] for p in grid["settled"]) + 1
            grid["shape"] = None
            return True

        new_shape.add(new_point)

    grid["shape"] = new_shape
    return False


def main():
    with open("input") as f:
        moves = f.read().strip()

    grid = {
        "settled": set(),
        "height": 0,
        "shape": None,
    }

    m = 0

    for i in range(2022):
        add_shape(grid, i % 5)

        while True:
            move = moves[m]
            m = (m + 1) % len(moves)

            move_shape(grid, move)
            settled = move_shape_down(grid)
            if settled:
                break

    print(grid["height"])


if __name__ == "__main__":
    main()
