#!/usr/bin/env python3

from collections import defaultdict


def main():
    with open("input") as f:
        line = f.read().strip()
        stones = [int(s) for s in line.split()]

    counts = defaultdict(int)
    for s in stones:
        counts[s] += 1

    for i in range(75):
        counts = blink(counts)

    print(sum(counts.values()))


def blink(counts):
    ret = defaultdict(int)

    for s, n in counts.items():
        ss = str(s)

        if s == 0:
            ret[1] += n
        elif len(ss) % 2 == 0:
            m = len(ss) // 2
            s1, s2 = ss[:m], ss[m:]
            ret[int(s1)] += n
            ret[int(s2)] += n
        else:
            ret[s * 2024] += n

    return ret


if __name__ == "__main__":
    main()
