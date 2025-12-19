#!/usr/bin/env python3


def main():
    seen = set()

    with open("input") as f:
        for line in f:
            num = int(line.strip())
            comp = 2020 - num
            if comp in seen:
                print(num * comp)
                break
            seen.add(num)


if __name__ == "__main__":
    main()
