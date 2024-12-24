#!/usr/bin/env python3

from functools import cache

import pyperclip
from lib.file import File

wires = {}
rules = {}


def main():
    with open("input") as f:
        ff = File(f)

        for line in ff.read_lines():
            k, v = line.split(": ")
            wires[k] = int(v)

        for line in ff.read_lines():
            a, b, c, d, e = line.split()
            assert e not in rules
            rules[e] = (a, b, c)

    z_keys = sorted([k for k in rules if k.startswith("z")])
    z_vals = [solve(k) for k in z_keys]

    ret = 0

    for v in reversed(z_vals):
        ret *= 2
        ret += v

    print(ret)
    pyperclip.copy(ret)


@cache
def solve(wire):
    if wire in wires:
        return wires[wire]

    a, b, c = rules[wire]
    av = solve(a)
    cv = solve(c)

    if b == "OR":
        return av | cv
    elif b == "AND":
        return av & cv
    elif b == "XOR":
        return av ^ cv

    raise ValueError


if __name__ == "__main__":
    main()
