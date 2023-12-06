#!/usr/bin/env python3


def main():
    with open("input") as f:
        times = list(map(int, f.readline().strip().split()[1:]))
        dists = list(map(int, f.readline().strip().split()[1:]))

    ret = 1

    for i in range(len(times)):
        t = times[i]
        d = dists[i]

        wins = 0
        for i in range(1, t):
            tot = i * (t-i)
            if tot > d:
                wins += 1
        ret *= wins

    print(ret)


if __name__ == "__main__":
    main()
