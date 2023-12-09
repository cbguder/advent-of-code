#!/usr/bin/env python3


def main():
    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            seq = list(map(int, line.split()))
            ret += next_val(seq)

    print(ret)


def next_val(seq):
    seqs = [seq]

    while True:
        cur = seqs[-1]
        if set(cur) == {0}:
            break

        seqs.append(diffs(cur))

    seqs[-1].insert(0, 0)
    i = len(seqs) - 2
    while i >= 0:
        seqs[i].insert(0, seqs[i][0] - seqs[i + 1][0])
        i -= 1

    return seqs[0][0]


def diffs(seq):
    return [
        seq[i + 1] - seq[i]
        for i in range(len(seq) - 1)
    ]


if __name__ == "__main__":
    main()
