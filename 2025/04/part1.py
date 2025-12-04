#!/usr/bin/env python3

import pyperclip
from lib.file import File
from lib.grid import Grid


def main():
    ret = 0

    with open("input") as f:
        ff = File(f)
        grid = ff.read_grid()

    for p, c in grid.items():
        if c == "@":
            neighbors = grid.neighbors(p, include_diagonal=True)
            rolls = len([n for n in neighbors if grid.at(n) == "@"])
            if rolls < 4:
                ret += 1

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
