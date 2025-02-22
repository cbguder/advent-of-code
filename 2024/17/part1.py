#!/usr/bin/env python3

import re

import pyperclip


def main():
    registers = {}
    program = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Register"):
                m = re.match(r"Register (\w+): (\d+)", line)
                registers[m[1]] = int(m[2])
            elif line.startswith("Program:"):
                program = [int(c) for c in line[9:].split(",")]

    ret = run(program, registers)
    ret = ",".join(str(r) for r in ret)

    print(ret)
    pyperclip.copy(ret)


def run(pr, reg):
    ip = 0
    ret = []

    while ip < len(pr):
        ins = pr[ip]
        op = pr[ip + 1]
        cmb = combo(op, reg)
        jumped = False

        match ins:
            case 0:
                reg["A"] = reg["A"] // (2**cmb)
            case 1:
                reg["B"] = reg["B"] ^ op
            case 2:
                reg["B"] = cmb % 8
            case 3:
                if reg["A"] != 0:
                    ip = op
                    jumped = True
            case 4:
                reg["B"] = reg["B"] ^ reg["C"]
            case 5:
                ret.append(cmb % 8)
            case 6:
                reg["B"] = reg["A"] // (2**cmb)
            case 7:
                reg["C"] = reg["A"] // (2**cmb)

        if not jumped:
            ip += 2

    return ret


def combo(op, reg):
    if op < 4:
        return op
    elif op == 4:
        return reg["A"]
    elif op == 5:
        return reg["B"]
    elif op == 6:
        return reg["C"]

    raise ValueError


if __name__ == "__main__":
    main()
