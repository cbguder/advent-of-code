#!/usr/bin/env python3

import re
import z3


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
    x = z3.Int("x")
    y = z3.Int("y")
    s = z3.Solver()
    s.add(x * a[0] + y * b[0] == p[0] + 10000000000000)
    s.add(x * a[1] + y * b[1] == p[1] + 10000000000000)

    if s.check() == z3.sat:
        model = s.model()
        return 3 * model[x].as_long() + model[y].as_long()

    return 0


if __name__ == "__main__":
    main()
