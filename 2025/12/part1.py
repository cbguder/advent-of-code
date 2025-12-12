#!/usr/bin/env python3

import pyperclip
from lib.file import File


def main():
    ret = 0

    regions = []
    shapes = []

    with open("input") as f:
        ff = File(f)

        while True:
            l = ff.read_line()

            if not l:
                break
            elif l[-1] == ":":
                g = ff.read_grid()
                shapes.append(g)
            else:
                raw_size, raw_to_fit = l.split(": ")
                size = tuple(map(int, raw_size.split("x")))
                to_fit = list(map(int, raw_to_fit.split()))
                regions.append((size, to_fit))

    for size, to_fit in regions:
        if can_fit(shapes, size, to_fit):
            ret += 1

    print(ret)
    pyperclip.copy(ret)


def can_fit(shapes, size, to_fit):
    space = size[0] * size[1]
    needed = 0

    for idx, count in enumerate(to_fit):
        shape_size = len([_ for _ in shapes[idx].find_all("#")])
        needed += shape_size * count

    return needed <= space


if __name__ == "__main__":
    main()
