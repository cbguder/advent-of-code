#!/usr/bin/env python3

from functools import cache

import pyperclip
from lib.grid import Grid
from lib.point import Point

NUM = Grid([["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]])

DIR = Grid([["#", "^", "A"], ["<", "v", ">"]])


def main():
    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            path = solve(line)
            val = int("".join([c for c in line if c in "0123456789"]))
            ret += path * val

    print(ret)
    pyperclip.copy(ret)


def solve(code):
    ret = 0

    prev = "A"
    for c in code:
        ret += shortest_pair_length(0, prev, c, 26)
        prev = c

    return ret


@cache
def shortest_pair_length(pad, start, end, level):
    paths = shortest_steps(pad, start, end)

    if level == 1:
        return len(paths[0])

    min_l = float("inf")

    for path in paths:
        path_l = 0
        prev = "A"
        for c in path:
            path_l += shortest_pair_length(1, prev, c, level - 1)
            prev = c

        min_l = min(min_l, path_l)

    return min_l


@cache
def shortest_steps(pad, start, end):
    if pad == 0:
        g = NUM
    else:
        g = DIR

    bad = g.find("#")
    sp = g.find(start)
    ep = g.find(end)
    d = ep - sp

    h = v = ""

    if d.x > 0:
        h = ">" * d.x
    elif d.x < 0:
        h = "<" * abs(d.x)

    if d.y > 0:
        v = "v" * d.y
    elif d.y < 0:
        v = "^" * abs(d.y)

    if h == "" or v == "":
        return [h + v + "A"]

    ret = []
    if sp + Point(d.x, 0) != bad:
        ret.append(h + v + "A")
    if sp + Point(0, d.y) != bad:
        ret.append(v + h + "A")

    return ret


if __name__ == "__main__":
    main()
