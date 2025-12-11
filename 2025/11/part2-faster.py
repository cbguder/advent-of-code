#!/usr/bin/env python3

from functools import cache

import pyperclip

g = {}


def main():
    global g

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split()
            src = parts[0][:-1]
            dests = parts[1:]
            g[src] = set(dests)

    ret = count_paths("svr", "fft")
    ret *= count_paths("fft", "dac")
    ret *= count_paths("dac", "out")

    print(ret)
    pyperclip.copy(ret)


@cache
def count_paths(src, dest):
    global g

    neighbors = g.get(src, set())

    if dest in neighbors:
        return 1

    ret = 0
    for nxt in neighbors:
        ret += count_paths(nxt, dest)

    return ret


if __name__ == "__main__":
    main()
