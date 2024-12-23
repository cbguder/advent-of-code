#!/usr/bin/env python3

import itertools

import networkx as nx
import pyperclip


def main():
    G = nx.Graph()

    with open("input") as f:
        for line in f:
            cmps = line.strip().split("-")
            G.add_nodes_from(cmps)
            G.add_edge(*cmps)

    ret = 0

    for clq in nx.find_cliques(G):
        if len(clq) < 3:
            continue

        for triple in itertools.combinations(clq, 3):
            if any(n for n in triple if n.startswith("t")):
                ret += 1

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
