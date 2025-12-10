#!/usr/bin/env python3

import pyperclip
import z3


def main():
    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split()
            machine = parts[0]
            buttons = parts[1:-1]
            ret += solve(machine, buttons)

    print(ret)
    pyperclip.copy(ret)


def solve(raw_machine, raw_buttons):
    res = tuple(1 if c == "#" else 0 for c in raw_machine[1:-1])

    n = len(res)

    buttons = []
    for raw_b in raw_buttons:
        b = [0] * n
        for flip in map(int, raw_b[1:-1].split(",")):
            b[flip] = 1
        buttons.append(tuple(b))

    return _solve(res, tuple(buttons))


def _solve(res, buttons):
    s = z3.Solver()
    n = len(res)

    cs = [z3.Int(f"c{i}") for i in range(len(buttons))]
    for c in cs:
        s.add(c >= 0)

    for i in range(n):
        terms = []
        for j, b in enumerate(buttons):
            if b[i] == 1:
                terms.append(cs[j])

        s.add(z3.Sum(terms) % 2 == res[i])

    ret = None

    while s.check() == z3.sat:
        m = s.model()
        ret = sum(m[c].as_long() for c in cs)
        s.add(z3.Sum(cs) < ret)

    return ret


if __name__ == "__main__":
    main()
