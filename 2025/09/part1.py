#!/usr/bin/env python3

import itertools

import pyperclip
from lib.file import File


def main():
    ret = 0

    with open("input") as f:
        ff = File(f)
        points = ff.read_points()

    for a, b in itertools.combinations(points, 2):
        d = abs(a - b)
        area = (d.x + 1) * (d.y + 1)
        ret = max(ret, area)

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
