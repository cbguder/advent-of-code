#!/usr/bin/env python3

from collections import defaultdict


def main():
    neighbors = defaultdict(set)

    with open('input') as f:
        for line in f:
            n1, n2 = line.strip().split('-')
            if n1 != 'start':
                neighbors[n2].add(n1)
            if n2 != 'start':
                neighbors[n1].add(n2)

    paths = {('start',)}
    complete_paths = set()

    while True:
        newpaths = enhance(paths, neighbors)
        next_paths = set()

        for newpath in newpaths:
            if newpath[-1] == 'end':
                complete_paths.add(newpath)
            else:
                next_paths.add(newpath)

        if next_paths == paths:
            break

        paths = next_paths

    print(len(complete_paths))


def enhance(paths, neighbors):
    newpaths = set()

    for path in paths:
        last_node = path[-1]
        for neighbor in neighbors[last_node]:
            newpath = path + (neighbor,)
            if not invalid_path(newpath):
                newpaths.add(newpath)

    return newpaths


def invalid_path(path):
    counts = defaultdict(int)
    repeats = set()

    for node in path:
        if node.islower():
            counts[node] += 1

            if counts[node] > 2:
                return True
            elif counts[node] == 2:
                repeats.add(node)
                if len(repeats) > 1:
                    return True

    return False


if __name__ == '__main__':
    main()
