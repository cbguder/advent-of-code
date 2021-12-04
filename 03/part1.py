#!/usr/bin/env python


def main():
    counts = None

    with open('input') as f:
        for line in f:
            line = line.strip()

            if counts is None:
                counts = []
                for i in range(len(line)):
                    counts.append({})

            for i in range(len(counts)):
                bit = line[i]
                counts[i][bit] = counts[i].get(bit, 0) + 1

    gamma = ''
    epsilon = ''

    for count in counts:
        if count['0'] > count['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    
    power = int(gamma, 2) * int(epsilon, 2)
    print(power)


if __name__ == '__main__':
    main()
