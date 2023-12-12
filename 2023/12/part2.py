#!/usr/bin/env python3

import re
from functools import lru_cache


def main():
    ret = 0

    with open("input") as f:
        for line in f:
            parts = line.strip().split()

            parts[0] = "?".join([parts[0]] * 5)
            sgrps = tuple(g for g in parts[0].split(".") if g != "")

            grps = tuple(map(int, parts[1].split(",")))
            grps *= 5

            ret += solve(sgrps, grps)

    print(ret)


@lru_cache
def solve(sgrps, grps):
    if len(sgrps) == 0:
        if len(grps) == 0:
            return 1
        else:
            return 0

    if set(sgrps[0]) == {"#"}:
        if grps and grps[0] == len(sgrps[0]):
            return solve(sgrps[1:], grps[1:])
        else:
            return 0

    m = re.match("^#+", sgrps[0])
    if m:
        if not grps or len(m.group(0)) > grps[0]:
            return 0

    # At least one question mark in sgrps[0]
    sgrps1 = (sgrps[0].replace("?", "#", 1),) + sgrps[1:]

    _sgrps2 = [x for x in sgrps[0].replace("?", ".", 1).split(".") if x != ""]
    sgrps2 = tuple(_sgrps2) + sgrps[1:]
    return solve(sgrps1, grps) + solve(sgrps2, grps)


if __name__ == "__main__":
    main()
