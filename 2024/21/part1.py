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
    p1 = shortest_paths(0, "A" + code)

    p2 = []
    for p in p1:
        p2 += shortest_paths(1, "A" + p)

    min_l = min([len(p) for p in p2])
    min_paths = [p for p in p2 if len(p) == min_l]

    p3 = []
    for p in min_paths:
        p3 += shortest_paths(1, "A" + p)

    min_l = min([len(p) for p in p3])
    return min_l


@cache
def shortest_paths(pad, code):
    if len(code) == 1:
        return [""]

    ret = []
    for p1 in shortest_steps(pad, code[0], code[1]):
        for p2 in shortest_paths(pad, code[1:]):
            ret.append(p1 + "A" + p2)

    min_l = min(len(p) for p in ret)
    return [p for p in ret if len(p) == min_l]


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
        return [h + v]

    ret = []
    if sp + Point(d.x, 0) != bad:
        ret.append(h + v)
    if sp + Point(0, d.y) != bad:
        ret.append(v + h)

    return ret


if __name__ == "__main__":
    main()
