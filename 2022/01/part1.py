#!/usr/bin/env python3


def main():
    max = 0

    with open("input") as f:
        elf = 0
        for line in f:
            line = line.strip()
            if line == "":
                elf = 0
            else:
                elf += int(line)
                if elf > max:
                    max = elf

    print(max)


if __name__ == "__main__":
    main()
