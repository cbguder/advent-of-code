#!/usr/bin/env python3

from functools import cache

import pyperclip


@cache
def _jolt(s, n):
    if n == 1:
        return max(s)
    elif n == len(s):
        return s

    a = s[0] + _jolt(s[1:], n - 1)
    b = _jolt(s[1:], n)

    if int(a) > int(b):
        return a
    else:
        return b


def jolt(line):
    return int(_jolt(line, 12))


def main():
    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            ret += jolt(line)

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
