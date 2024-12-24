#!/usr/bin/env python3

from functools import cache, reduce

import pyperclip
from lib.file import File

wires = {}
rules = {}
exp = {}


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

    swaps = set()
    while True:
        swap = try_with(swaps)
        if swap is None:
            break
        swaps.add(swap)

    ret = ",".join(sorted(flatten(swaps)))
    print(ret)
    pyperclip.copy(ret)


def try_with(swaps):
    exp.clear()

    z_wires = sorted([k for k in rules if k.startswith("z")])
    for i, kz in enumerate(z_wires[:-1]):
        act = expand(kz, tuple(swaps))
        equal(act, expected(i))

    if len(exp) == 0:
        return None

    swapped_wires = flatten(swaps)

    for w1, exp_w1 in exp.items():
        if w1 in swapped_wires:
            continue

        for w2 in rules:
            if w1 == w2:
                continue

            if w2 in swapped_wires:
                continue

            act_w2 = expand(w2, tuple(swaps))
            if equal(act_w2, exp_w1):
                return w1, w2

    raise RuntimeError


def flatten(swaps):
    return reduce(lambda x, y: x | set(y), swaps, set())


@cache
def expected(n):
    kx = "x{:02}".format(n)
    ky = "y{:02}".format(n)

    ret = ("XOR", kx, ky, None)
    if n > 0:
        ret = ("XOR", ret, (carry(n - 1)), None)

    return ret


@cache
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
    if not ret and l1 not in exp:
        exp[l1] = (o2, a2, c2, l2)

    return ret


@cache
def expand(wire, swaps):
    if wire in wires:
        return wire

    for w1, w2 in swaps:
        if w1 == wire:
            wire = w2
        elif w2 == wire:
            wire = w1

    a, op, c = rules[wire]
    av = expand(a, swaps)
    cv = expand(c, swaps)
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


if __name__ == "__main__":
    main()
