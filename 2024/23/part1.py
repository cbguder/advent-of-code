#!/usr/bin/env python3

import itertools

import pyperclip


def main():
    edges = set()
    nodes = set()

    with open("input") as f:
        for line in f:
            line = line.strip()
            cmps = line.split("-")
            nodes.update(cmps)
            edges.add(tuple(sorted(cmps)))

    ret = 0

    for triple in itertools.combinations(sorted(nodes), 3):
        if connected(triple, edges):
            ret += 1

    print(ret)
    pyperclip.copy(ret)


def connected(nodes, edges):
    if len([n for n in nodes if n.startswith("t")]) == 0:
        return False

    for n1, n2 in itertools.combinations(nodes, 2):
        if (n1, n2) not in edges:
            return False

    return True


if __name__ == "__main__":
    main()
