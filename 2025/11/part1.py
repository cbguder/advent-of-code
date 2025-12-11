#!/usr/bin/env python3

import networkx as nx
import pyperclip


def main():
    G = nx.DiGraph()

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split()
            src = parts[0][:-1]
            for dest in parts[1:]:
                G.add_edge(src, dest)

    paths = nx.all_simple_paths(G, "you", "out")
    ret = len([p for p in paths])

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
