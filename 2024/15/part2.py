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
                w = len(line) * 2
                h = y + 1
                for x, c in enumerate(line):
                    if c == "@":
                        bot = (y, 2 * x)
                    elif c == "O":
                        boxes.add((y, 2 * x))
                    elif c == "#":
                        walls.add((y, 2 * x))
                        walls.add((y, 2 * x + 1))
                y += 1

    while moves:
        m = moves.pop(0)

        dx, dy = 0, 0
        if m == "<":
            dx = -1
        elif m == ">":
            dx = 1
        elif m == "^":
            dy = -1
        elif m == "v":
            dy = 1

        can_move = True
        by, bx = bot
        ny, nx = by + dy, bx + dx
        to_add = set()
        to_remove = set()
        if m == "<":
            for x in range(nx, -1, -1):
                if (by, x) in boxes:
                    to_add.add((by, x - 1))
                    to_remove.add((by, x))
                elif (by, x - 1) in boxes:
                    continue
                elif (by, x) in walls:
                    can_move = False
                    break
                else:
                    break
        elif m == ">":
            for x in range(nx, w + 1):
                if (by, x) in boxes:
                    to_add.add((by, x + 1))
                    to_remove.add((by, x))
                elif (by, x - 1) in boxes:
                    continue
                elif (by, x) in walls:
                    can_move = False
                    break
                else:
                    break
        elif m == "^":
            xrange = {bx}
            for y in range(ny, -1, -1):
                new_xrange = set()
                for x in xrange:
                    if (y, x) in boxes:
                        to_add.add((y - 1, x))
                        to_remove.add((y, x))
                        new_xrange.update({x, x + 1})
                    elif (y, x - 1) in boxes:
                        to_add.add((y - 1, x - 1))
                        to_remove.add((y, x - 1))
                        new_xrange.update({x - 1, x})
                    elif (y, x) in walls:
                        can_move = False
                        break
                if not new_xrange or not can_move:
                    break
                xrange = new_xrange
        elif m == "v":
            xrange = {bx}
            for y in range(ny, h + 1):
                new_xrange = set()
                for x in xrange:
                    if (y, x) in boxes:
                        to_add.add((y + 1, x))
                        to_remove.add((y, x))
                        new_xrange.update({x, x + 1})
                    elif (y, x - 1) in boxes:
                        to_add.add((y + 1, x - 1))
                        to_remove.add((y, x - 1))
                        new_xrange.update({x - 1, x})
                    elif (y, x) in walls:
                        can_move = False
                        break
                if not new_xrange or not can_move:
                    break
                xrange = new_xrange

        if can_move:
            boxes.difference_update(to_remove)
            boxes.update(to_add)
            bot = (ny, nx)

    ret = sum(100 * b[0] + b[1] for b in boxes)

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
