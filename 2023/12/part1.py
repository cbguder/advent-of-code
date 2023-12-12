#!/usr/bin/env python3

import re
from itertools import product


def main():
    ret = 0

    with open("input") as f:
        for line in f:
            parts = line.strip().split()
            grps = list(map(int, parts[1].split(",")))
            res = solve(parts[0], grps)
            ret += res

    print(ret)


def solve(line, grps):
    sgrps = [g for g in line.split(".") if g != ""]

    ret = 0

    for agrp in alternate(sgrps):
        if count(agrp) == grps:
            ret += 1

    return ret


def subalternate(s):
    if len(s) == 0:
        yield ""
        return

    if "?" not in s:
        yield s
        return

    if s[0] == "?":
        for ss in subalternate(s[1:]):
            yield "#" + ss
            yield "." + ss
        return

    for ss in subalternate(s[1:]):
        yield s[0] + ss


def alternate(sgrps):
    return product(*[subalternate(s) for s in sgrps])


def count(sgrps):
    ret = []
    for s in sgrps:
        parts = re.split(r"[^#]", s)
        parts = [p for p in parts if p != ""]
        ret += list(map(len, parts))
    return ret


if __name__ == "__main__":
    main()
