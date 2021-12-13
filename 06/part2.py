#!/usr/bin/env python3


from collections import defaultdict


def main():
    fish = defaultdict(int)

    with open('input') as f:
        lines = f.readlines()

    for f in map(int, lines[0].split(',')):
        fish[f] += 1

    for i in range(256):
        newfish = defaultdict(int)

        for k, v in fish.items():
            if k == 0:
                newfish[6] += v
                newfish[8] += v
            else:
                newfish[k - 1] += v

        fish = newfish

    print(sum(fish.values()))


if __name__ == '__main__':
    main()
