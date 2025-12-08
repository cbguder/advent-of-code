#!/usr/bin/env python3

import itertools

import networkx as nx
import pyperclip
from lib.file import File


def main():
    with open("input") as f:
        ff = File(f)
        points = ff.read_points_3d()

    G = nx.Graph()
    G.add_nodes_from(points)

    dists = []
    for a, b in itertools.combinations(points, 2):
        dist = a.distance(b)
        dists.append((dist, a, b))

    dists.sort()
    for i in range(1000):
        _, a, b = dists[i]
        G.add_edge(a, b)

    ret = 1
    for c in sorted(nx.connected_components(G), key=len, reverse=True)[:3]:
        ret *= len(c)

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
