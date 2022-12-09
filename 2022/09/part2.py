#!/usr/bin/env python3


def touching(head, tail):
    xdif = abs(head[0] - tail[0])
    ydif = abs(head[1] - tail[1])
    return xdif < 2 and ydif < 2


def main():
    knots = []
    for i in range(10):
        knots.append((0, 0))

    tail_locs = {(0, 0)}

    with open("input") as f:
        for line in f:
            line = line.strip()
            direction, steps = tuple(line.split())
            steps = int(steps)

            for i in range(steps):
                head = knots[0]

                if direction == "U":
                    head = (head[0], head[1] + 1)
                elif direction == "D":
                    head = (head[0], head[1] - 1)
                elif direction == "R":
                    head = (head[0] + 1, head[1])
                elif direction == "L":
                    head = (head[0] - 1, head[1])

                knots[0] = head

                for j in range(9):
                    leader = knots[j]
                    follower = knots[j+1]

                    if touching(leader, follower):
                        break

                    if leader[0] == follower[0]:
                        if leader[1] > follower[1]:
                            follower = (follower[0], follower[1] + 1)
                        elif leader[1] < follower[1]:
                            follower = (follower[0], follower[1] - 1)
                    elif leader[1] == follower[1]:
                        if leader[0] > follower[0]:
                            follower = (follower[0] + 1, follower[1])
                        elif leader[0] < follower[0]:
                            follower = (follower[0] - 1, follower[1])
                    else:
                        if leader[0] > follower[0]:
                            if leader[1] > follower[1]:
                                follower = (follower[0] + 1, follower[1] + 1)
                            else:
                                follower = (follower[0] + 1, follower[1] - 1)
                        else:
                            if leader[1] > follower[1]:
                                follower = (follower[0] - 1, follower[1] + 1)
                            else:
                                follower = (follower[0] - 1, follower[1] - 1)

                    knots[j] = leader
                    knots[j+1] = follower

                tail_locs.add(knots[-1])

    print(len(tail_locs))


if __name__ == "__main__":
    main()
