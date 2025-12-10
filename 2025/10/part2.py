#!/usr/bin/env python3

import pyperclip
import z3


def main():
    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split()
            buttons = parts[1:-1]
            joltage = parts[-1]
            ret += solve(joltage, buttons)

    print(ret)
    pyperclip.copy(ret)


def solve(raw_joltage, raw_buttons):
    joltage = tuple(map(int, raw_joltage[1:-1].split(",")))

    n = len(joltage)

    buttons = []
    for raw_b in raw_buttons:
        b = [0] * n
        for flip in map(int, raw_b[1:-1].split(",")):
            b[flip] = 1
        buttons.append(tuple(b))

    return _solve(joltage, tuple(buttons))


def _solve(joltage, buttons):
    s = z3.Solver()
    n = len(joltage)

    cs = [z3.Int(f"c{i}") for i in range(len(buttons))]
    for c in cs:
        s.add(c >= 0)

    for i in range(n):
        terms = []
        for j, b in enumerate(buttons):
            if b[i] == 1:
                terms.append(cs[j])

        s.add(z3.Sum(terms) == joltage[i])

    ret = None

    while s.check() == z3.sat:
        m = s.model()
        ret = sum(m[c].as_long() for c in cs)
        s.add(z3.Sum(cs) < ret)

    return ret


if __name__ == "__main__":
    main()
