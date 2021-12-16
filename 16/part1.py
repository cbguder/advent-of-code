#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Packet:
    version: int
    type: int

    def version_sum(self):
        return self.version


@dataclass(frozen=True)
class Literal(Packet):
    value: int


@dataclass(frozen=True)
class Operator(Packet):
    subpackets: List[Packet]

    def version_sum(self):
        return self.version + sum([p.version_sum() for p in self.subpackets])


def main():
    with open('input') as f:
        input = f.read().strip()

    width = len(input) * 4
    bitstr = format(int(input, 16), f"0{width}b")
    packet, _ = read_packet(bitstr)

    print(packet.version_sum())


def read_num(n, bitstr):
    bits, rest = read_bits(n, bitstr)
    val = int(bits, 2)

    return val, rest


def read_bits(n, bitstr):
    assert len(bitstr) >= n

    bits = bitstr[:n]
    rest = bitstr[n:]

    return bits, rest


def read_packet(bitstr):
    version, rest = read_num(3, bitstr)
    type, rest = read_num(3, rest)

    if type == 4:
        value, rest = read_literal(rest)
        packet = Literal(version, type, value)
    else:
        subpackets, rest = read_operator(rest)
        packet = Operator(version, type, subpackets)

    return packet, rest


def read_literal(bitstr):
    val = 0

    rest = bitstr
    while True:
        val = val << 4

        v, rest = read_num(5, rest)
        if v >= 16:
            val += v % 16
        else:
            val += v
            break

    return val, rest


def read_operator(bitstr):
    length_type, rest = read_num(1, bitstr)
    subs = []

    if length_type == 0:
        length, rest = read_num(15, rest)
        sub_bits, rest = read_bits(length, rest)
        while len(sub_bits) > 0 and "1" in sub_bits:
            sub, sub_bits = read_packet(sub_bits)
            subs.append(sub)
    else:
        num_subs, rest = read_num(11, rest)
        for i in range(num_subs):
            sub, rest = read_packet(rest)
            subs.append(sub)

    return subs, rest


if __name__ == '__main__':
    main()
