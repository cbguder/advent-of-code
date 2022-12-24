#!/usr/bin/env python3

from collections import defaultdict


def move_blizzards(blizzards, w, h):
    new_blizzards = defaultdict(list)

    for pos, dirs in blizzards.items():
        for d in dirs:
            nx, ny = pos

            if d == ">":
                nx += 1
            elif d == "<":
                nx -= 1
            elif d == "v":
                ny += 1
            elif d == "^":
                ny -= 1

            nx %= w
            ny %= h

            new_blizzards[(nx, ny)].append(d)

    return new_blizzards


def neighbors(pos, w, h):
    if pos == (0, -1):
        return {
            pos,
            (0, 0),
        }

    neighs = {pos}

    x, y = pos

    if x > 0:
        neighs.add((x - 1, y))
    if x < w - 1:
        neighs.add((x + 1, y))
    if y > 0:
        neighs.add((x, y - 1))
    if y < h - 1:
        neighs.add((x, y + 1))

    if x == w - 1 and y == h - 1:
        neighs.add((x, y + 1))

    return neighs


def main():
    blizzards = defaultdict(list)

    with open("input") as f:
        y = 0

        for line in f:
            line = line.strip()
            for x, ch in enumerate(line):
                if ch in "<>v^":
                    blizzards[(x - 1, y - 1)].append(ch)
            y += 1

    w = len(line) - 2
    h = y - 2
    start = (0, -1)
    dest = (w - 1, h)

    locs = {start}
    t = 0

    while dest not in locs:
        new_locs = set()
        new_blizzards = move_blizzards(blizzards, w, h)

        for loc in locs:
            for opt in neighbors(loc, w, h):
                if opt not in new_blizzards:
                    new_locs.add(opt)

        locs = new_locs
        blizzards = new_blizzards
        t += 1

    print(t)


if __name__ == "__main__":
    main()
