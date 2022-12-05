#!/usr/bin/env python3


import re


MOVE_RE = r"move (\d+) from (\d+) to (\d+)"


def main():
    stacks = []

    for i in range(9):
        stacks.append([])

    with open("input") as f:
        for line in f:
            if line.startswith("["):
                for i in range(9):
                    crate = line[1 + i * 4]
                    if crate != " ":
                        stacks[i] = [crate] + stacks[i]
            else:
                match = re.match(MOVE_RE, line)
                if match is not None:
                    count = int(match.group(1))
                    from_crate = int(match.group(2))
                    to_crate = int(match.group(3))

                    boxes = []
                    for i in range(count):
                        box = stacks[from_crate-1].pop()
                        boxes.append(box)
                    boxes.reverse()
                    for box in boxes:
                        stacks[to_crate-1].append(box)

    tops = [stack[-1] for stack in stacks]
    print("".join(tops))


if __name__ == "__main__":
    main()
