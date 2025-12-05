#!/usr/bin/env python3

import pyperclip

from lib.file import File


def main():
    ret = 0

    with open("input") as f:
        ff = File(f)

        ranges = [tuple(map(int, r)) for r in ff.read_multi_lines("-")]
        ranges.sort()

    merged = [ranges[0]]
    for start, end in ranges[1:]:
        if start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
        else:
            merged.append((start, end))

    for start, end in merged:
        ret += end - start + 1

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
