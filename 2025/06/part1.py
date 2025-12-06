#!/usr/bin/env python3
from functools import reduce

import pyperclip
from lib.file import File
from lib.grid import Grid


def main():
    ret = 0

    rows = []
    with open("input") as f:
        for line in f:
            line = line.strip()
            rows.append(line.split())

    g = Grid(rows)
    for i in range(g.width):
        col = g.column(i)
        if col[-1] == "+":
            ret += sum(map(int, col[:-1]))
        elif col[-1] == "*":
            ret += reduce(lambda a, b: int(a) * int(b), col[:-1])

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
