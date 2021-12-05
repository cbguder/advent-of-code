#!/usr/bin/env python3

def main():
    prev = None
    increased = 0

    with open('input') as f:
        for line in f:
            measurement = int(line)
            if prev is not None:
                if measurement > prev:
                    increased += 1
            prev = measurement

    print(increased)


if __name__ == '__main__':
    main()
