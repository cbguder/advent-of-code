#!/usr/bin/env python3

import re


def main():
    with open("input") as f:
        data = f.read().strip()
        parts = data.split("\n\n")

    ret = 0
    for p in parts:
        lines = p.split("\n")
        m = re.match(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])
        a = int(m.group(1)), int(m.group(2))

        m = re.match(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])
        b = int(m.group(1)), int(m.group(2))

        m = re.match(r"Prize: X=(\d+), Y=(\d+)", lines[2])
        p = int(m.group(1)), int(m.group(2))

        ret += solve(a, b, p)

    print(ret)


def solve(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p

    px += 10000000000000
    py += 10000000000000

    ad = (ax * by) - (ay * bx)
    pd = (px * by) - (py * bx)

    if pd % ad == 0:
        ar = pd // ad
        br = (px - ax * ar) // bx
        return 3 * ar + br

    return 0


if __name__ == "__main__":
    main()
