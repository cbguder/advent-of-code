#!/usr/bin/env python3

import pyperclip
from lib.file import File


def main():
    ret = 0

    with open("input") as f:
        ff = File(f)

        ranges = [tuple(map(int, r)) for r in ff.read_multi_lines("-")]

        for idx in ff.read_lines():
            for start, end in ranges:
                if start <= int(idx) <= end:
                    ret += 1
                    break

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
