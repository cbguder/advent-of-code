#!/usr/bin/env python3

MAX = 99_999_999_999_999
MIN = 11_111_111_111_111


def main():
    with open("input") as f:
        instrs = [line.strip().split() for line in f]

    stack = [MIN]

    while True:
        num = stack.pop(0)
        inp = _num_to_digits(num)

        best_mutation, zval = find_best_mutation(inp, instrs)
        mut_num = _digits_to_num(best_mutation)
        if zval == 0:
            print(mut_num)
            break

        stack.append(mut_num)


def all_mutations(inp):
    for i in range(14):
        for sub in set(range(2, 10)) - {inp[i]}:
            new_inp = inp[:]
            new_inp[i] = sub
            yield new_inp


def find_best_mutation(inp, instrs):
    lowest_zval = float("inf")
    best_mutation = None

    for new_inp in all_mutations(inp):
        num = _digits_to_num(new_inp)

        regs = run(instrs, new_inp)
        if regs["z"] < lowest_zval:
            lowest_zval = regs["z"]
            best_mutation = new_inp

    return best_mutation, lowest_zval


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
