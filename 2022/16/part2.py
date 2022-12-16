#!/usr/bin/env python3


import re
from dataclasses import dataclass
from typing import Set

nodes = {}
cache = {}
best = 0


@dataclass(frozen=True)
class Node:
    flow: int
    neighbors: Set[str]


def find_flow(loc1, loc2, t, flow, opens):
    global best

    loc1, loc2 = sorted([loc1, loc2])
    cache_key = (t, loc1, loc2)
    if cache.get(cache_key, -1) >= flow:
        return
    cache[cache_key] = flow

    if t == 0:
        if flow > best:
            best = flow
        return

    if len(opens) == len(nodes):
        find_flow(loc1, loc2, t - 1, flow, opens)
        return

    node1 = nodes[loc1]
    node2 = nodes[loc2]

    opt_keys = {"MOVE_MOVE"}

    open1_option = loc1 not in opens
    if open1_option:
        opt_keys.add("OPEN_MOVE")

    if loc1 != loc2:
        open2_option = loc2 not in opens

        if open2_option:
            opt_keys.add("MOVE_OPEN")

        if open1_option and open2_option:
            opt_keys.add("OPEN_OPEN")

    t -= 1

    if "OPEN_OPEN" in opt_keys:
        new_flow = flow
        new_flow += (t * node1.flow)
        new_flow += (t * node2.flow)
        find_flow(loc1, loc2, t, new_flow, opens | {loc1, loc2})
    if "OPEN_MOVE" in opt_keys:
        new_flow = flow + (t * node1.flow)
        for neighbor in node2.neighbors | {loc2}:
            find_flow(loc1, neighbor, t, new_flow, opens | {loc1})
    if "MOVE_OPEN" in opt_keys:
        new_flow = flow + (t * node2.flow)
        for neighbor in node1.neighbors | {loc1}:
            find_flow(loc2, neighbor, t, new_flow, opens | {loc2})
    if "MOVE_MOVE" in opt_keys:
        for n1 in node1.neighbors | {loc1}:
            for n2 in node2.neighbors | {loc2}:
                find_flow(n1, n2, t, flow, opens)


def main():
    global nodes, best

    opens = set()

    with open("input") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line)
            valve = m.group(1)
            flow = int(m.group(2))
            if flow == 0:
                opens.add(valve)
            neighbors = set(m.group(3).split(", "))
            node = Node(flow=flow, neighbors=neighbors)
            nodes[valve] = node

    find_flow("AA", "AA", 26, 0, opens)
    print(best)


if __name__ == "__main__":
    main()
