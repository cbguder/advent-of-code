#!/usr/bin/env python3

import pyperclip


def main():
    ret = 0

    with open("input") as f:
        patterns = f.readline().strip().split(", ")
        f.readline()

        for line in f:
            line = line.strip()

            if possible(line, patterns):
                ret += 1

    print(ret)
    pyperclip.copy(ret)


def possible(line, patterns):
    if line == "":
        return True

    for pattern in patterns:
        if line.startswith(pattern):
            if possible(line[len(pattern):], patterns):
                return True

    return False


if __name__ == "__main__":
    main()
