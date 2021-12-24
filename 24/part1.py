#!/usr/bin/env python3

import bisect


def main():
    with open("input") as f:
        instrs = [line.strip().split() for line in f]

    inp = [9] * 14
    regs = run(instrs, inp)

    stack = [(regs["z"], _digits_to_num(inp))]

    while True:
        _, prev = stack.pop(0)
        digs = _num_to_digits(prev)
        for i in range(14):
            for sub in set(range(1, 10)) - {digs[i]}:
                new_digs = digs[:]
                new_digs[i] = sub
                num = _digits_to_num(new_digs)

                regs = run(instrs, new_digs)
                if regs["z"] == 0:
                    print(num)
                    return

                bisect.insort(stack, (regs["z"], num))


def _num_to_digits(num):
    return list(map(int, str(num)))


def _digits_to_num(digits):
    return int("".join(map(str, digits)))


def run(instrs, input_digits):
    input_digits = input_digits.copy()

    regs = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    def _val(arg):
        if arg in regs:
            return regs[arg]
        return int(arg)

    for instr in instrs:
        op = instr[0]
        args = instr[1:]

        if op == "inp":
            regs[args[0]] = input_digits.pop(0)
        elif op == "add":
            regs[args[0]] += _val(args[1])
        elif op == "mul":
            regs[args[0]] *= _val(args[1])
        elif op == "div":
            regs[args[0]] //= _val(args[1])
        elif op == "mod":
            regs[args[0]] %= _val(args[1])
        elif op == "eql":
            regs[args[0]] = int(regs[args[0]] == _val(args[1]))

    return regs


if __name__ == "__main__":
    main()
