#!/usr/bin/env python3

from collections import defaultdict


def main():
    neighbors = defaultdict(set)
    edges = set()

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split(": ")
            src = parts[0]
            dests = parts[1].split()
            for dest in dests:
                edges.add(tuple(sorted([src, dest])))
                neighbors[src].add(dest)
                neighbors[dest].add(src)

    # After trying to brute force this, and (unsuccessfully) messing around with
    # Karger's algorithm, I gave up and just visualized the graph using Graphviz.
    # print("graph G {")
    # for src, dest in edges:
    #     print(f"  {src} -- {dest};")
    # print("}")

    to_remove = {("gzr", "qnz"), ("hgk", "pgz"), ("lmj", "xgs")}
    start = list(neighbors.keys())[0]
    seen = find_connected(neighbors, start, to_remove)
    n1 = len(seen)
    n2 = len(neighbors) - n1
    print(n1 * n2)


def find_connected(neighbors, start, removed):
    seen = set()
    queue = [start]

    while queue:
        cur = queue.pop()
        if cur in seen:
            continue
        seen.add(cur)

        for n in neighbors[cur]:
            if tuple(sorted([cur, n])) not in removed:
                queue.append(n)

    return seen


if __name__ == "__main__":
    main()
