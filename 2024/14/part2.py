#!/usr/bin/env python3

import re
import png


def main():
    w, h = 101, 103

    bots = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"p=(.*),(.*) v=(.*),(.*)", line)
            p = (int(m[1]), int(m[2]))
            v = (int(m[3]), int(m[4]))
            bots.append((p, v))

    states = {tuple(bots)}
    secs = 0
    while True:
        secs += 1

        for i, (p, v) in enumerate(bots):
            p = (
                (p[0] + v[0]) % w,
                (p[1] + v[1]) % h,
            )
            bots[i] = (p, v)

        s = tuple(bots)
        if s in states:
            break

        if secs % w == 14:
            print_grid(bots, secs, w, h)


def print_grid(bots, secs, w, h):
    grid = {p for (p, v) in bots}

    img = []
    for y in range(h):
        row = []
        for x in range(w):
            if (x, y) in grid:
                row += [0, 0, 0]
            else:
                row += [255, 255, 255]
        img.append(row)

    with open("{}.png".format(secs), 'wb') as f:
        w = png.Writer(w, h, greyscale=False)
        w.write(f, img)


if __name__ == "__main__":
    main()
