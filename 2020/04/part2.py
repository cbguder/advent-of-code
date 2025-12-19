#!/usr/bin/env python3
import re

import pyperclip
from lib.file import File

REQUIRED_FIELDS = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}


def is_valid(p):
    for field in REQUIRED_FIELDS:
        if field not in p:
            return False

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not (1920 <= int(p["byr"]) <= 2002):
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if not (2010 <= int(p["iyr"]) <= 2020):
        return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not (2020 <= int(p["eyr"]) <= 2030):
        return False

    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    hgt = p["hgt"]
    if hgt.endswith("cm"):
        if not (150 <= int(hgt[:-2]) <= 193):
            return False
    elif hgt.endswith("in"):
        if not (59 <= int(hgt[:-2]) <= 76):
            return False
    else:
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not re.match(r"^#[0-9a-f]{6}$", p["hcl"]):
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if not p["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid = p["pid"]
    if len(pid) != 9 or not pid.isdigit():
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
