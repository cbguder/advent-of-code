#!/usr/bin/env python3

from functools import cache, reduce

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

    swaps = [("z12", "djg"), ("z19", "sbg"), ("hjm", "mcq"), ("z37", "dsd")]
    for w1, w2 in swaps:
        rules[w1], rules[w2] = rules[w2], rules[w1]

    z_wires = sorted([k for k in rules if k.startswith("z")])
    bits = len(z_wires)

    for i in range(bits - 1):
        kz = "z{:02}".format(i)
        exp = expected(i)
        act = expand(kz)
        equal(act, exp)

    ret = ",".join(sorted(reduce(lambda x, y: x | set(y), swaps, set())))
    print(ret)
    pyperclip.copy(ret)


def expected(n):
    kx = "x{:02}".format(n)
    ky = "y{:02}".format(n)

    ret = ("XOR", kx, ky, None)
    if n > 0:
        ret = ("XOR", ret, (carry(n - 1)), None)

    return ret


def carry(n):
    if n == 0:
        return "AND", "x00", "y00", None

    kx = "x{:02}".format(n)
    ky = "y{:02}".format(n)
    _, a, c, _ = expected(n)
    return "OR", ("AND", kx, ky, None), ("AND", a, c, None), None


def equal(t1, t2):
    if isinstance(t1, str) or isinstance(t2, str):
        return t1 == t2

    o1, a1, c1, l1 = normalize(t1)
    o2, a2, c2, l2 = normalize(t2)

    ret = (o1 == o2) and equal(a1, a2) and equal(c1, c2)
    if not ret:
        print(l1, "NOT AS EXPECTED")
        print("ACT:", print_tree((o1, a1, c1, l1)))
        print("EXP:", print_tree((o2, a2, c2, l2)))
        print("----------------------------")

    return ret


@cache
def expand(wire):
    if wire in wires:
        return wire

    a, op, c = rules[wire]
    av = expand(a)
    cv = expand(c)
    return op, av, cv, wire


@cache
def normalize(t):
    if isinstance(t, str):
        return t

    op, av, cv, l = t
    av = normalize(av)
    cv = normalize(cv)

    astr = str(av)
    cstr = str(cv)

    if len(astr) > len(cstr):
        av, cv = cv, av
    elif len(astr) == len(cstr):
        if astr > cstr:
            av, cv = cv, av

    return op, av, cv, l


def print_tree(t):
    if isinstance(t, str):
        return t

    a, b, c, _ = normalize(t)
    return "({} {} {})".format(a, print_tree(b), print_tree(c))


if __name__ == "__main__":
    main()
