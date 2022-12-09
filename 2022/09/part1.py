#!/usr/bin/env python3


def touching(head, tail):
    xdif = abs(head[0] - tail[0])
    ydif = abs(head[1] - tail[1])
    return xdif < 2 and ydif < 2


def main():
    head = (0, 0)
    tail = (0, 0)
    tail_locs = {tail}

    with open("input") as f:
        for line in f:
            line = line.strip()
            direction, steps = tuple(line.split())
            steps = int(steps)

            for i in range(steps):
                if direction == "U":
                    head = (head[0], head[1] + 1)
                elif direction == "D":
                    head = (head[0], head[1] - 1)
                elif direction == "R":
                    head = (head[0] + 1, head[1])
                elif direction == "L":
                    head = (head[0] - 1, head[1])

                if touching(head, tail):
                    continue

                if head[0] == tail[0]:
                    if head[1] > tail[1]:
                        tail = (tail[0], tail[1] + 1)
                    elif head[1] < tail[1]:
                        tail = (tail[0], tail[1] - 1)
                elif head[1] == tail[1]:
                    if head[0] > tail[0]:
                        tail = (tail[0] + 1, tail[1])
                    elif head[0] < tail[0]:
                        tail = (tail[0] - 1, tail[1])
                else:
                    if head[0] > tail[0]:
                        if head[1] > tail[1]:
                            tail = (tail[0] + 1, tail[1] + 1)
                        else:
                            tail = (tail[0] + 1, tail[1] - 1)
                    else:
                        if head[1] > tail[1]:
                            tail = (tail[0] - 1, tail[1] + 1)
                        else:
                            tail = (tail[0] - 1, tail[1] - 1)

                tail_locs.add(tail)

    print(len(tail_locs))


if __name__ == "__main__":
    main()
