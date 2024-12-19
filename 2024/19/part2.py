#!/usr/bin/env python3

from functools import cache

import pyperclip

patterns = []


def main():
    global patterns
    ret = 0

    with open("input") as f:
        patterns = f.readline().strip().split(", ")
        f.readline()

        for line in f:
            line = line.strip()
            ret += possible(line)

    print(ret)
    pyperclip.copy(ret)


@cache
def possible(line):
    if line == "":
        return 1

    ret = 0
    for pattern in patterns:
        if line.startswith(pattern):
            ret += possible(line[len(pattern):])

    return ret


if __name__ == "__main__":
    main()
