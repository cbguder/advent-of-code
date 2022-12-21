#!/usr/bin/env python3
import re


def solve(vals, ops, name):
    if name in vals:
        return vals[name]

    n1, op, n2 = ops[name]

    a = solve(vals, ops, n1)
    b = solve(vals, ops, n2)

    if op == "+":
        val = a + b
    elif op == "-":
        val = a - b
    elif op == "*":
        val = a * b
    elif op == "/":
        val = a / b
    else:
        assert False

    vals[name] = val
    return val


def main():
    vals = {}
    ops = {}

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split(": ")
            name = parts[0]

            if re.match(r"\d+", parts[1]):
                vals[name] = int(parts[1])
            else:
                m = re.match(r"(\w+) (.) (\w+)", parts[1])
                ops[name] = m.groups()

    print(solve(vals, ops, "root"))


if __name__ == "__main__":
    main()
