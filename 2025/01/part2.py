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

            prev = p
            ret += n // 100
            n %= 100

            if dir == "R":
                p += n
            else:
                p -= n

            if p <= 0 < prev or p >= 100:
                ret += 1

            p %= 100

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
