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
    elif pos == (w - 1, h):
        return {
            pos,
            (w - 1, h - 1),
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

    if pos == (w - 1, h - 1):
        neighs.add((x, y + 1))
    elif pos == (0, 0):
        neighs.add((0, -1))

    return neighs


def run(start, dest, blizzards, w, h):
    t = 0
    locs = {start}

    while dest not in locs:
        if not locs:
            raise RuntimeError("Ran out of locations")
        elif t > 100000:
            raise RuntimeError("Too many iterations")

        new_locs = set()
        new_blizzards = move_blizzards(blizzards, w, h)

        for loc in locs:
            for opt in neighbors(loc, w, h):
                if opt not in new_blizzards:
                    new_locs.add(opt)

        locs = new_locs
        blizzards = new_blizzards
        t += 1

    return t, blizzards


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

    t1, blizzards = run(start, dest, blizzards, w, h)
    t2, blizzards = run(dest, start, blizzards, w, h)
    t3, blizzards = run(start, dest, blizzards, w, h)

    print(t1 + t2 + t3)


if __name__ == "__main__":
    main()
