#!/usr/bin/env python3

import pyperclip


def invalid_ids(start, end):
    for n in range(start, end + 1):
        if invalid_id(n):
            yield n


def invalid_id(n):
    s = str(n)
    l = len(s)
    for d in range(1, l // 2 + 1):
        if l % d != 0:
            continue
        t = set()
        for i in range(0, l, d):
            t.add(s[i:i + d])
        if len(t) == 1:
            return True

    return False


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
