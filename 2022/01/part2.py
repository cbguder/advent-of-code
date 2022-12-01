#!/usr/bin/env python3


def main():
    elves = []

    with open("input") as f:
        elf = 0
        for line in f:
            line = line.strip()
            if line == "":
                elves.append(elf)
                elf = 0
            else:
                elf += int(line)

    elves.sort(reverse=True)
    print(sum(elves[:3]))


if __name__ == "__main__":
    main()
