#!/usr/bin/env python3


def main():
    x = 1
    t = 0
    total = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split()

            if parts[0] == "noop":
                t += 1
                if t in {20, 60, 100, 140, 180, 220}:
                    total += t * x
            elif parts[0] == "addx":
                t += 1
                if t in {20, 60, 100, 140, 180, 220}:
                    total += t * x
                t += 1
                if t in {20, 60, 100, 140, 180, 220}:
                    total += t * x
                x += int(parts[1])

    print(total)


if __name__ == "__main__":
    main()
