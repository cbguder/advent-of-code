#!/usr/bin/env python3

import itertools

import networkx as nx
import pyperclip


def main():
    ret = 0

    G = nx.DiGraph()

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split()
            src = parts[0][:-1]
            for dest in parts[1:]:
                G.add_edge(src, dest)

    groups = [
        {"svr"},
        {"kxy", "nju", "xed"},
        {"uyb", "qlj", "oyz", "yhv"},
        {"xyw", "mfc", "bjj", "cin"},
        {"bid", "cub", "ooa", "jcy"},
        {"ykg", "tgk", "cjp", "you"},
        {"out"},
    ]

    G2 = nx.DiGraph()
    for g1, g2 in itertools.pairwise(groups):
        for a in g1:
            for b in g2:
                G2.add_edge(a, b)

    for meta_path in nx.all_simple_paths(G2, "svr", "out"):
        paths = 1
        for a, b in itertools.pairwise(meta_path):
            if not nx.has_path(G, a, b):
                continue

            # Remove all edges from all nodes in b's group
            g2 = [g for g in groups if b in g][0]
            edges_bak = []
            for src in g2:
                for dest in G[src]:
                    edges_bak.append((src, dest))
            G.remove_edges_from(edges_bak)

            if a in {"kxy", "nju", "xed"}:
                paths *= len([p for p in nx.all_simple_paths(G, a, b) if "fft" in p])
            elif a in {"bid", "cub", "ooa", "jcy"}:
                paths *= len([p for p in nx.all_simple_paths(G, a, b) if "dac" in p])
            else:
                paths *= len([_ for _ in nx.all_simple_paths(G, a, b)])

            # Re-add edges
            G.add_edges_from(edges_bak)

        ret += paths

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
