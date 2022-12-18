#!/usr/bin/env python3

from itertools import combinations


def touching(c1, c2):
    return sorted([
        abs(c1[0] - c2[0]),
        abs(c1[1] - c2[1]),
        abs(c1[2] - c2[2]),
    ]) == [0, 0, 1]


def main():
    cubes = []
    surface = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            cubes.append(tuple(map(int, line.split(","))))
            surface += 6

    for c1, c2 in combinations(cubes, 2):
        if touching(c1, c2):
            surface -= 2

    print(surface)


if __name__ == "__main__":
    main()
