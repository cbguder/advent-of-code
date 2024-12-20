#!/usr/bin/env python3

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

    G = nx.Graph()

    for pt, ch in grid.items():
        if ch == "#":
            continue

        G.add_node(pt)

        for n in grid.neighbors(pt):
            if grid.at(n) == "#":
                continue

            G.add_edge(pt, n)

    s = grid.find("S")
    e = grid.find("E")

    sp_list = nx.shortest_path(G, s, e)
    ret = 0

    for i, n1 in enumerate(tqdm(sp_list)):
        for j, n2 in enumerate(sp_list[i + 1 :]):
            d = abs(n1 - n2)
            dist = d.x + d.y

            if dist > 20:
                continue

            savings = j - dist + 1
            if savings >= 100:
                ret += 1

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
