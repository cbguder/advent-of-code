#!/usr/bin/env python3

import pyperclip

from lib.grid import Grid
from lib.point import Point


def main():
    moves = []
    grid = None
    rows = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            if line == "":
                grid = Grid(rows)
            elif grid is not None:
                moves += [c for c in line]
            else:
                rows.append([c for c in line])

    bot = grid.find("@")
    while moves:
        match moves.pop(0):
            case "<":
                d = Point(-1, 0)
            case ">":
                d = Point(1, 0)
            case "^":
                d = Point(0, -1)
            case "v":
                d = Point(0, 1)

        if move(grid, bot, d):
            bot += d

    ret = 0
    for box in grid.find_all("O"):
        ret += 100 * box.y + box.x

    print(ret)
    pyperclip.copy(ret)


def move(grid, p, d):
    v = grid.at(p)
    if v == ".":
        return True
    elif v == "#":
        return False

    nxt = p + d
    if not move(grid, nxt, d):
        return False

    grid.set(nxt, v)
    grid.set(p, ".")
    return True


if __name__ == "__main__":
    main()
