#!/usr/bin/env python3
from functools import reduce

import pyperclip
from lib.file import File
from lib.grid import Grid


def main():
    ret = 0

    with open("input") as f:
        rows = [l.rstrip() for l in f]

    width = max(len(r) for r in rows)
    for i, row in enumerate(rows):
        rows[i] = pad(row, width)

    g = Grid(rows)

    cols = []
    for i in range(width):
        col = g.column(i)
        if not "".join(col).strip():
            ret += process(cols)
            cols = []
        else:
            cols.append(col)
    ret += process(cols)

    print(ret)
    pyperclip.copy(ret)


def pad(s, length):
    return s + " " * (length - len(s))


def process(cols):
    nums = (int("".join(c[:-1])) for c in cols)

    if cols[0][-1] == "+":
        return sum(nums)
    else:
        return reduce(lambda a, b: a * b, nums)


if __name__ == "__main__":
    main()
