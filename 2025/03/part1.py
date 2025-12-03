#!/usr/bin/env python3

import pyperclip


def jolt(line):
    ret = 0
    for i, x in enumerate(line):
        for y in line[i + 1:]:
            n = 10 * int(x) + int(y)
            ret = max(ret, n)
    return ret


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
