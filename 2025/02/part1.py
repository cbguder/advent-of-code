#!/usr/bin/env python3

import pyperclip


def invalid_ids(start, end):
    for n in range(start, end + 1):
        s = str(n)
        l = len(s)
        if l % 2 != 0:
            continue
        if s[:l // 2] == s[l // 2:]:
            yield n


def main():
    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split(",")
            for p in parts:
                start, end = p.split("-")
                for n in invalid_ids(int(start), int(end)):
                    ret += n

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
