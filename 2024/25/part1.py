#!/usr/bin/env python3

import pyperclip
from lib.file import File
from lib.point import Point


def main():
    grids = []

    with open("input") as f:
        ff = File(f)
        while True:
            g = ff.read_grid()
            if g.height == 0:
                break
            grids.append(g)

    locks = []
    keys = []

    H = grids[0].height
    W = grids[0].width

    for g in grids:
        heights = []
        for x in range(W):
            col = g.column(x)
            heights.append(col.count("#") - 1)

        if g.at(Point(0, 0)) == "#":
            locks.append(heights)
        elif g.at(Point(0, H - 1)) == "#":
            keys.append(heights)

    ret = 0
    for lock in locks:
        for key in keys:
            fits = True
            for x in range(W):
                if lock[x] + key[x] > H - 2:
                    fits = False
                    break
            if fits:
                ret += 1

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
