#!/usr/bin/env python3

from collections import defaultdict

import pyperclip
from lib.file import File
from lib.point import Point


def main():
    ret = 0

    with open("input") as f:
        ff = File(f)
        g = ff.read_grid()

    beams = defaultdict(int)
    for p, c in g.items():
        if c == "S":
            beams[p] += 1

    while beams:
        next_beams = defaultdict(int)

        for b, c in beams.items():
            next = b + Point(0, 1)
            if g.in_bounds(next):
                if g.at(next) == "^":
                    ret += 1
                    left = next + Point(-1, 0)
                    if g.in_bounds(left):
                        next_beams[left] += c
                    right = next + Point(1, 0)
                    if g.in_bounds(right):
                        next_beams[right] += c
                else:
                    next_beams[next] += c

        if not next_beams:
            ret = sum(beams.values())

        beams = next_beams

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
