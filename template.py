#!/usr/bin/env python3

import pyperclip


def main():
    with open("input") as f:
        for line in f:
            line = line.strip()
            pass

    ret = 0

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
