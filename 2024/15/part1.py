#!/usr/bin/env python3

import pyperclip


def main():
    moves = []
    y = 0
    w = 0
    h = 0
    bot = None
    boxes = set()
    walls = set()
    grid_done = False

    with open("input") as f:
        for line in f:
            line = line.strip()
            if line == "":
                grid_done = True
            elif grid_done:
                moves += [c for c in line]
            else:
                w = len(line)
                h = y + 1
                for x, c in enumerate(line):
                    if c == "@":
                        bot = (y, x)
                    elif c == "O":
                        boxes.add((y, x))
                    elif c == "#":
                        walls.add((y, x))
                y += 1

    while moves:
        m = moves.pop(0)
        by, bx = bot

        box_ahead = []
        room = 0
        dx, dy = 0, 0
        if m == "<":
            wx = max(w[1] for w in walls if w[0] == by and w[1] < bx)
            box_ahead = [b for b in boxes if b[0] == by and wx < b[1] < bx]
            room = bx - wx - 1
            dx = -1
        elif m == ">":
            wx = min(w[1] for w in walls if w[0] == by and w[1] > bx)
            box_ahead = [b for b in boxes if b[0] == by and bx < b[1] < wx]
            room = wx - bx - 1
            dx = 1
        elif m == "^":
            wy = max(w[0] for w in walls if w[1] == bx and w[0] < by)
            box_ahead = [b for b in boxes if b[1] == bx and wy < b[0] < by]
            room = by - wy - 1
            dy = -1
        elif m == "v":
            wy = min(w[0] for w in walls if w[1] == bx and w[0] > by)
            box_ahead = [b for b in boxes if b[1] == bx and by < b[0] < wy]
            room = wy - by - 1
            dy = 1

        if room > len(box_ahead):
            ny, nx = by + dy, bx + dx
            bot = (ny, nx)

            to_add = set()
            if m == "<":
                for x in range(nx, 0, -1):
                    if (by, x) in boxes:
                        to_add.add((by, x - 1))
                        boxes.remove((by, x))
                    else:
                        break
            elif m == ">":
                for x in range(nx, w):
                    if (by, x) in boxes:
                        to_add.add((by, x + 1))
                        boxes.remove((by, x))
                    else:
                        break
            elif m == "^":
                for y in range(ny, 0, -1):
                    if (y, bx) in boxes:
                        to_add.add((y - 1, bx))
                        boxes.remove((y, bx))
                    else:
                        break
            elif m == "v":
                for y in range(ny, h):
                    if (y, bx) in boxes:
                        to_add.add((y + 1, bx))
                        boxes.remove((y, bx))
                    else:
                        break

            boxes.update(to_add)

    ret = sum(100 * b[0] + b[1] for b in boxes)

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
