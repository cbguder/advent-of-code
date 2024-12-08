#!/usr/bin/env python3

from collections import defaultdict
from itertools import pairwise, permutations


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
            d = (l1[0] - l2[0], l1[1] - l2[1])

            a1 = (l1[0] + d[0], l1[1] + d[1])
            a2 = (l2[0] - d[0], l2[1] - d[1])

            if 0 <= a1[0] < h and 0 <= a1[1] < w:
                antinodes.add(a1)
            if 0 <= a2[0] < h and 0 <= a2[1] < w:
                antinodes.add(a2)

    print(len(antinodes))


if __name__ == "__main__":
    main()
