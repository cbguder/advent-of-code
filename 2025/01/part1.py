#!/usr/bin/env python3

import pyperclip


def main():
    ret = 0
    p = 50

    with open("input") as f:
        for line in f:
            line = line.strip()
            dir = line[0]
            n = int(line[1:])
            if dir == "R":
                p += n
            else:
                p -= n
            p %= 100
            if p == 0:
                ret += 1

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
