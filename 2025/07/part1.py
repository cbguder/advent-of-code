#!/usr/bin/env python3

import pyperclip
from lib.file import File
from lib.point import Point


def main():
    ret = 0

    with open("input") as f:
        ff = File(f)
        g = ff.read_grid()

    beams = set()
    for p, c in g.items():
        if c == "S":
            beams.add(p)

    while beams:
        next_beams = set()

        for b in beams:
            next = b + Point(0, 1)
            if g.in_bounds(next):
                if g.at(next) == "^":
                    ret += 1
                    left = next + Point(-1, 0)
                    if g.in_bounds(left):
                        next_beams.add(left)
                    right = next + Point(1, 0)
                    if g.in_bounds(right):
                        next_beams.add(right)
                else:
                    next_beams.add(next)

        beams = next_beams

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
