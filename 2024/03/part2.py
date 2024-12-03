#!/usr/bin/env python3

import re


def main():
    ret = 0
    do = True
    with open("input") as f:
        data = f.read()
        for m in re.finditer(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", data):
            if m[0] == "do()":
                do = True
            elif m[0] == "don't()":
                do = False
            elif do:
                x, y = m[0][4:-1].split(",")
                ret += int(x) * int(y)

    print(ret)


if __name__ == "__main__":
    main()
