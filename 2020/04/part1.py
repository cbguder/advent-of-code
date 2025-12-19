#!/usr/bin/env python3

import pyperclip
from lib.file import File

REQUIRED_FIELDS = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}


def is_valid(p):
    for field in REQUIRED_FIELDS:
        if field not in p:
            return False

    return True


def main():
    passports = []

    with open("input") as f:
        ff = File(f)
        while lines := ff.read_lines():
            passport = {}

            for line in lines:
                parts = line.split()
                for part in parts:
                    key, val = part.split(":")
                    passport[key] = val

            passports.append(passport)

    ret = len([p for p in passports if is_valid(p)])

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
