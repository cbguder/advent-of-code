#!/usr/bin/env python3

from itertools import pairwise


def main():
    pos = (0, 0)
    pts = [(0, 0)]

    x_vals = {0}
    y_vals = {0}

    h_lines = []
    v_lines = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split()

            dr, dist, code = parts

            dist = int(code[2:7], 16)
            dr = int(code[7], 16)

            end = add(pos, dr, dist)
            pts.append(end)

            x_vals.add(end[1])
            y_vals.add(end[0])

            if dr == 0 or dr == 2:
                min_x = min(pos[1], end[1])
                max_x = max(pos[1], end[1])
                h_lines.append((pos[0], min_x, max_x))
            else:
                min_y = min(pos[0], end[0])
                max_y = max(pos[0], end[0])
                v_lines.append((pos[1], min_y, max_y))

            pos = end

    h_lines.sort()
    v_lines.sort()

    y_ord = sorted(list(y_vals))
    x_ord = sorted(list(x_vals))

    ret = 0

    for y1, y2 in pairwise(y_ord):
        for x1, x2 in pairwise(x_ord):
            hcount = len([l for l in h_lines if l[0] <= y1 and l[1] <= x1 and x2 <= l[2]])
            vcount = len([l for l in v_lines if l[0] <= x1 and l[1] <= y1 and y2 <= l[2]])

            inside = hcount % 2 == 1 or vcount % 2 == 1
            if inside:
                ret += (y2 - y1) * (x2 - x1)

    bord = 0
    for p1, p2 in pairwise(pts):
        if p1[0] == p2[0]:
            bord += abs(p1[1] - p2[1]) / 2.0
        elif p1[1] == p2[1]:
            bord += abs(p1[0] - p2[0]) / 2.0

    print(ret + bord + 1)


def add(pos, dr, dist):
    y, x = pos

    if dr == 0:
        return (y, x + dist)
    elif dr == 2:
        return (y, x - dist)
    elif dr == 3:
        return (y - dist, x)
    elif dr == 1:
        return (y + dist, x)

    assert False


if __name__ == "__main__":
    main()
