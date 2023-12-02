#!/usr/bin/env python3


def main():
    tot = 0

    with open("input") as f:
        for line in f:
            line = line.strip()

            parts = line.split(":")

            colors = {"red": 0, "green": 0, "blue": 0}

            for turn in parts[1].split(";"):
                turn = turn.strip()
                turn_parts = turn.split(",")

                for part in turn_parts:
                    part = part.strip()
                    num, color = part.split(" ")
                    if int(num) > colors[color]:
                        colors[color] = int(num)

            res = 1
            for n in colors.values():
                res *= n

            tot += res

    print(tot)


if __name__ == "__main__":
    main()
