#!/usr/bin/env python3

import re


def main():
    ret = 0
    with open("input") as f:
        data = f.read()
        for m in re.findall(r"mul\(\d{1,3},\d{1,3}\)", data):
            x, y = m[4:-1].split(",")
            ret += int(x) * int(y)

    print(ret)


if __name__ == "__main__":
    main()
