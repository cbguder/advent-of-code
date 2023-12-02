#!/usr/bin/env python3


colors = {"red": 12, "green": 13, "blue": 14}


def main():
    tot = 0

    with open("input") as f:
        for line in f:
            line = line.strip()

            parts = line.split(":")
            game_num = int(parts[0][5:])

            if game_possible(parts[1]):
                tot += game_num

    print(tot)


def game_possible(turns):
    for turn in turns.split(";"):
        turn = turn.strip()
        turn_parts = turn.split(",")

        for part in turn_parts:
            part = part.strip()
            num, color = part.split(" ")
            if int(num) > colors[color]:
                return False

    return True


if __name__ == "__main__":
    main()
