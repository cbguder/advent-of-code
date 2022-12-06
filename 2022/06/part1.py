#!/usr/bin/env python3


def main():
    with open("input") as f:
        for line in f:
            line = line.strip()
            break

    for i in range(len(line)):
        if len(set(line[i:i+4])) == 4:
            print(i+4)
            return


if __name__ == "__main__":
    main()
