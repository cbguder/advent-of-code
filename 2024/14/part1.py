#!/usr/bin/env python3

import re


def simulate(p, v, w, h):
    return (
        (p[0] + (v[0] * 100)) % w,
        (p[1] + (v[1] * 100)) % h,
    )


def quad(pos, w, h):
    mid_w = w // 2
    mid_h = h // 2

    if pos[0] == mid_w or pos[1] == mid_h:
        return -1

    q = 0
    if pos[0] > mid_w:
        q += 1
    if pos[1] > mid_h:
        q += 2

    return q


def main():
    w, h = 101, 103

    quads = [0, 0, 0, 0]

    with open("input") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"p=(.*),(.*) v=(.*),(.*)", line)
            p = (int(m[1]), int(m[2]))
            v = (int(m[3]), int(m[4]))
            pos = simulate(p, v, w, h)
            q = quad(pos, w, h)
            if q >= 0:
                quads[q] += 1

    ret = quads[0] * quads[1] * quads[2] * quads[3]
    print(ret)


if __name__ == "__main__":
    main()
