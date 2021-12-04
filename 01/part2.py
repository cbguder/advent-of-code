#!/usr/bin/env python

def main():
    prev = []
    increased = 0

    with open('input') as f:
        for line in f:
            measurement = int(line)
            if len(prev) >= 3:
                if measurement > prev[0]:
                    increased += 1
                prev = prev[1:]
            prev.append(measurement)

    print(increased)


if __name__ == '__main__':
    main()
