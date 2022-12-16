#!/usr/bin/env python3


import re
from dataclasses import dataclass
from typing import Set


@dataclass(frozen=True)
class Node:
    flow: int
    neighbors: Set[str]


cache = {}


def find_flow(nodes, start, t, open):
    if t <= 0:
        return 0

    cache_key = (start, t, tuple(sorted(list(open))))
    if cache_key in cache:
        return cache[cache_key]

    node = nodes[start]
    options = []

    if start not in open and node.flow > 0:
        opt = find_flow(nodes, start, t - 1, open | {start})
        opt += (t - 1) * node.flow
        options.append(opt)

    for neighbor in node.neighbors:
        opt = find_flow(nodes, neighbor, t - 1, open)
        options.append(opt)

    if not options:
        ret = 0
    else:
        ret = max(options)

    cache[cache_key] = ret
    return ret


def main():
    nodes = {}

    with open("input") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line)
            valve = m.group(1)
            flow = int(m.group(2))
            neighbors = set(m.group(3).split(", "))
            node = Node(flow=flow, neighbors=neighbors)
            nodes[valve] = node

    highest_flow = find_flow(nodes, "AA", 30, set())
    print(highest_flow)


if __name__ == "__main__":
    main()
