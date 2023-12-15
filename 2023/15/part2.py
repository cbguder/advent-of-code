#!/usr/bin/env python3
from collections import defaultdict


def main():
    boxes = [{}] * 256
    order = defaultdict(list)

    with open("input") as f:
        for line in f:
            line = line.strip()
            for p in line.split(","):
                if "=" in p:
                    label, val = p.split("=")
                    val = int(val)
                    box = h(label)

                    if label in boxes[box]:
                        boxes[box][label] = val
                    else:
                        boxes[box][label] = val
                        order[box].append(label)
                elif p.endswith("-"):
                    label = p[:-1]
                    box = h(label)
                    if label in boxes[box]:
                        del boxes[box][label]
                        order[box].remove(label)
                else:
                    assert False

    ret = 0

    for i in range(256):
        for j, lens in enumerate(order[i]):
            focus = i + 1
            focus *= j + 1
            focus *= boxes[i][lens]
            ret += focus

    print(ret)


def h(s):
    ret = 0
    for c in s:
        ret = (17 * (ret + ord(c))) % 256
    return ret


if __name__ == "__main__":
    main()
