#!/usr/bin/env python3


def main():
    with open("input") as f:
        t = int("".join(f.readline().strip().split()[1:]))
        d = int("".join(f.readline().strip().split()[1:]))

    wins = 0
    for i in range(1, t):
        tot = i * (t - i)
        if tot > d:
            wins += 1
    print(wins)


if __name__ == "__main__":
    main()
