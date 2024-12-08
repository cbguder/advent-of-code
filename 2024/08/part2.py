#!/usr/bin/env python3

from collections import defaultdict
from itertools import permutations


def main():
    locs = defaultdict(set)

    with open("input") as f:
        y = 0
        for line in f:
            line = line.strip()
            w = len(line)
            for x, c in enumerate(line):
                if c != ".":
                    locs[c].add((y, x))
            y += 1

    h = y

    antinodes = set()

    for c, l in locs.items():
        for l1, l2 in permutations(l, 2):
            antinodes.add(l1)
            antinodes.add(l2)

            d = (l1[0] - l2[0], l1[1] - l2[1])

            i = 1
            while True:
                a = (l2[0] + d[0] * i, l2[1] + d[1] * i)
                if 0 <= a[0] < h and 0 <= a[1] < w:
                    antinodes.add(a)
                    i += 1
                else:
                    break

            i = 1
            while True:
                a = (l1[0] - d[0] * i, l1[1] - d[1] * i)
                if 0 <= a[0] < h and 0 <= a[1] < w:
                    antinodes.add(a)
                    i += 1
                else:
                    break

    print(len(antinodes))


if __name__ == "__main__":
    main()
