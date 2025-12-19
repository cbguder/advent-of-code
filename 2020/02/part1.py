#!/usr/bin/env python3

import re


def main():
    valids = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
            low, high, char, password = m.groups()
            count = password.count(char)
            if int(low) <= count <= int(high):
                valids += 1

    print(valids)


if __name__ == "__main__":
    main()
