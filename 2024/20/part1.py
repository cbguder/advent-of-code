#!/usr/bin/env python3
import itertools

import networkx as nx
import pyperclip
from lib.grid import Grid
from tqdm import tqdm


def main():
    rows = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            rows.append([c for c in line])

    grid = Grid(rows)
    cheats = set()

    G = nx.Graph()

    for pt, ch in grid.items():
        if ch == "#":
            dots = set()

            for n in grid.neighbors(pt):
                if grid.at(n) in {".", "S", "E"}:
                    dots.add(n)

            for n1, n2 in itertools.combinations(dots, 2):
                if n1.x == n2.x or n1.y == n2.y:
                    cheats.add(tuple(sorted([n1, n2])))
        else:
            G.add_node(pt)

            for n in grid.neighbors(pt):
                if grid.at(n) == "#":
                    continue

                G.add_edge(pt, n)

    s = grid.find("S")
    e = grid.find("E")

    sp_list = nx.shortest_path(G, s, e)
    sp_set = set(sp_list)
    ret = 0

    for n1, n2 in tqdm(cheats):
        if n1 not in sp_set or n2 not in sp_set:
            continue

        savings = nx.shortest_path_length(G, n1, n2) - 2
        if savings >= 100:
            ret += 1

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
