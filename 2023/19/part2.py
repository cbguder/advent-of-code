#!/usr/bin/env python3

import re
from collections import defaultdict


def main():
    flows = {}

    with open("input") as f:
        for line in f:
            line = line.strip()

            if line == "":
                break

            m = re.match(r"(\w+)\{(.+)}", line)
            label, raw_flow = m.groups()
            parts1 = raw_flow.split(",")
            parts2 = [p.split(":") for p in parts1]
            for i in range(len(parts2)):
                if len(parts2[i]) > 1:
                    s = re.split(r"([<>])", parts2[i][0])
                    parts2[i] = s + [parts2[i][-1]]
            flows[label] = parts2

    queue = [
        ("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})
    ]
    a_parts = []

    while queue:
        cur, part = queue.pop(0)

        if cur == "A":
            a_parts.append(part)
            continue

        if cur == "R":
            continue

        for step in flows[cur]:
            if len(step) == 1:
                queue.append((step[0], part))
            else:
                part1, part2 = split_part_by_step(part, step)
                if part1 is not None:
                    queue.append((step[3], part1))
                if part2 is not None:
                    part = part2
                else:
                    break

    tot = sum(ways(part) for part in a_parts)
    print(tot)


def ways(part):
    ret = 1
    for v in part.values():
        ret *= v[1] - v[0] + 1
    return ret


def split_part_by_step(part, step):
    key, op, val = step[0], step[1], int(step[2])
    assert op in {"<", ">"}

    p1 = part.copy()
    p2 = part.copy()

    rng = part[key]

    if step[1] == "<":
        if rng[0] <= val <= rng[1]:
            p1[key] = (rng[0], val - 1)
            p2[key] = (val, rng[1])
        elif val > rng[1]:
            return part, None
        elif val < rng[0]:
            return None, part
    elif step[1] == ">":
        if rng[0] <= val <= rng[1]:
            p1[key] = (val + 1, rng[1])
            p2[key] = (rng[0], val)
        elif val > rng[1]:
            return None, part
        elif val < rng[0]:
            return part, None

    if not valid_range(p1[key]):
        p1 = None

    if not valid_range(p2[key]):
        p2 = None

    return p1, p2


def valid_range(rng):
    return rng[0] <= rng[1]


if __name__ == "__main__":
    main()
