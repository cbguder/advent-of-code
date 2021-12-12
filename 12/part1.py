#!/usr/bin/env python3

from collections import defaultdict


def main():
    neighbors = defaultdict(set)

    with open('input') as f:
        for line in f:
            n1, n2 = line.strip().split('-')
            neighbors[n1].add(n2)
            neighbors[n2].add(n1)

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
            if neighbor.isupper() or neighbor not in path:
                newpaths.add(path + (neighbor,))

    return newpaths


if __name__ == '__main__':
    main()
