#!/usr/bin/env python3

import networkx as nx
import pyperclip


def main():
    G = nx.Graph()

    with open("input") as f:
        for line in f:
            cmps = line.strip().split("-")
            G.add_nodes_from(cmps)
            G.add_edge(*cmps)

    clqs = sorted(nx.find_cliques(G), key=len)
    ret = ",".join(sorted(clqs[-1]))

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
