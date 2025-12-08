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

    ret = None

    for _, a, b in dists:
        G.add_edge(a, b)
        if nx.is_connected(G):
            ret = a.x * b.x
            break

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
