#!/usr/bin/env python3

import re


def main():
    valids = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
            low, high, char, password = m.groups()
            low_c = password[int(low) - 1]
            high_c = password[int(high) - 1]
            if (low_c == char) ^ (high_c == char):
                valids += 1

    print(valids)


if __name__ == "__main__":
    main()
