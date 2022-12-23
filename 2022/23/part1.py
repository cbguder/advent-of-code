#!/usr/bin/env python3
from collections import defaultdict


def neighbors(elf, dir=None):
    elves = []

    if dir == "N":
        for x in range(elf[0] - 1, elf[0] + 2):
            elves.append((x, elf[1] - 1))
    elif dir == "S":
        for x in range(elf[0] - 1, elf[0] + 2):
            elves.append((x, elf[1] + 1))
    elif dir == "W":
        for y in range(elf[1] - 1, elf[1] + 2):
            elves.append((elf[0] - 1, y))
    elif dir == "E":
        for y in range(elf[1] - 1, elf[1] + 2):
            elves.append((elf[0] + 1, y))
    else:
        for x in range(elf[0] - 1, elf[0] + 2):
            for y in range(elf[1] - 1, elf[1] + 2):
                if (x, y) != elf:
                    elves.append((x, y))

    return elves


def propose(elves, dirs, elf):
    neighs = neighbors(elf)

    if set(neighs).isdisjoint(elves):
        return None

    for dir in dirs:
        dir_neighs = neighbors(elf, dir)
        if set(dir_neighs).isdisjoint(elves):
            return dir_neighs[1]

    return None


def step(elves, dirs):
    new_elves = set()

    proposed = defaultdict(set)

    for elf in elves:
        new_loc = propose(elves, dirs, elf)
        if new_loc is None:
            new_elves.add(elf)
        else:
            proposed[new_loc].add(elf)

    for new_loc, elves in proposed.items():
        if len(elves) == 1:
            new_elves.add(new_loc)
        else:
            new_elves.update(elves)

    new_dirs = dirs[1:] + dirs[0:1]
    return new_elves, new_dirs


def main():
    elves = set()
    dirs = ["N", "S", "W", "E"]

    with open("input") as f:
        y = 0
        for line in f:
            line = line.strip()
            for x, ch in enumerate(line):
                if ch == "#":
                    elves.add((x, y))
            y += 1

    for _ in range(10):
        elves, dirs = step(elves, dirs)

    min_x = min(e[0] for e in elves)
    max_x = max(e[0] for e in elves)
    min_y = min(e[1] for e in elves)
    max_y = max(e[1] for e in elves)

    w = max_x - min_x + 1
    h = max_y - min_y + 1

    print(w * h - len(elves))


if __name__ == "__main__":
    main()
