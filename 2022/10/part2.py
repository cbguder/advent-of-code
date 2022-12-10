#!/usr/bin/env python3


def main():
    buf = []
    for i in range(6):
        buf.append([" "] * 40)

    x = 1
    t = 0

    def draw():
        row = t // 40
        col = t % 40
        if x - 1 <= col <= x + 1:
            buf[row][col] = "#"

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split()

            if parts[0] == "noop":
                draw()
                t += 1
            elif parts[0] == "addx":
                draw()
                t += 1
                draw()
                t += 1
                x += int(parts[1])

    for row in buf:
        print("".join(row))


if __name__ == "__main__":
    main()
