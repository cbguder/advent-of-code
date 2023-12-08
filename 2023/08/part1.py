#!/usr/bin/env python3

import re


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

    i = 0
    cur = "AAA"
    while True:
        dir = dirs[i % len(dirs)]
        cur = nodes[cur][dir]
        if cur == "ZZZ":
            break
        i += 1
    print(i + 1)


if __name__ == "__main__":
    main()
