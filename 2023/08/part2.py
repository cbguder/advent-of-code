#!/usr/bin/env python3

import re
from functools import reduce


def main():
    nodes = {}

    with open("input") as f:
        dirs = f.readline().strip()
        f.readline()

        for line in f:
            line = line.strip()
            m = re.match(r"(.+) = \((.+), (.+)\)", line)
            node, left, right = m.groups()
            nodes[node] = {"L": left, "R": right}

    starts = [n for n in nodes if n.endswith("A")]
    lens = {}

    for cur in starts:
        i = 0
        while True:
            dir = dirs[i % len(dirs)]
            cur = nodes[cur][dir]
            if cur.endswith("Z"):
                break
            i += 1
        lens[cur] = i + 1

    print(lcmm(*lens.values()))


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)


if __name__ == "__main__":
    main()
