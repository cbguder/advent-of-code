#!/usr/bin/env python3


def main():
    numbers = []

    with open('input') as f:
        numbers = [line.strip() for line in f]

    oxygen = numbers[:]
    co2 = numbers[:]

    for i in range(len(numbers[0])):
        oxygen = filter_bits(oxygen, i, '1')
        co2 = filter_bits(co2, i, '0')

    assert len(oxygen) == 1
    assert len(co2) == 1

    oxygen = int(oxygen[0], 2)
    co2 = int(co2[0], 2)

    print(oxygen * co2)


def count_bits(numbers, pos):
    counts = {'0': 0, '1': 0}

    for number in numbers:
        bit = number[pos]
        counts[bit] += 1

    return counts


def filter_bits(numbers, pos, preferred_bit):
    if len(numbers) == 1:
        return numbers

    counts = count_bits(numbers, pos)

    filter_bit = preferred_bit
    if counts['0'] > counts['1']:
        if preferred_bit == '0':
            filter_bit = '1'
        else:
            filter_bit = '0'

    ret = []
    for number in numbers:
        if number[pos] == filter_bit:
            ret.append(number)
    return ret


if __name__ == '__main__':
    main()
