#!/usr/bin/env python3

import pyperclip
from lib.file import File
from lib.grid import Grid


def main():
    ret = 0

    with open("input") as f:
        ff = File(f)
        grid = ff.read_grid()

    to_remove = set()

    while True:
        for p, c in grid.items():
            if c == "@":
                neighbors = grid.neighbors(p, include_diagonal=True)
                rolls = len([n for n in neighbors if grid.at(n) == "@"])
                if rolls < 4:
                    to_remove.add(p)

        if not to_remove:
            break

        for p in to_remove:
            grid.set(p, ".")

        ret += len(to_remove)
        to_remove.clear()

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
