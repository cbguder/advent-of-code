#!/usr/bin/env python3


import networkx as nx
import pyperclip
from lib.point import Point

M = 70
N = 1024


def main():
    points = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            x, y = tuple(map(int, line.split(",")))
            points.append(Point(x, y))

    mx = len(points)
    mn = 1024

    while True:
        if mx == mn:
            break

        n = (mx + mn) // 2
        blocks = set(points[:n])

        try:
            solve(blocks)
        except nx.exception.NetworkXNoPath:
            mx = n - 1
        else:
            mn = n + 1

    pt = points[mn]
    ret = "{},{}".format(pt.x, pt.y)
    print(ret)
    pyperclip.copy(ret)


def solve(blocks):
    G = nx.Graph()

    for y in range(M + 1):
        for x in range(M + 1):
            pt = Point(x, y)

            if pt in blocks:
                continue

            G.add_node((x, y))

            neighbors = [
                pt + Point(1, 0),
                pt + Point(0, 1),
                pt + Point(-1, 0),
                pt + Point(0, -1),
            ]

            for n in neighbors:
                if n in blocks:
                    continue

                if n.x < 0 or n.x > M:
                    continue

                if n.y < 0 or n.y > M:
                    continue

                G.add_edge((x, y), (n.x, n.y))

    return nx.astar_path_length(G, (0, 0), (M, M))


if __name__ == "__main__":
    main()
