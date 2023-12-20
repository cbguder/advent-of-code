#!/usr/bin/env python3

from collections import defaultdict


def main():
    mods = {}

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split(" -> ")
            name = parts[0]
            dest = parts[1].split(", ")
            typ = None

            if name.startswith("&") or name.startswith("%"):
                typ = name[0]
                name = name[1:]

            mod = {
                "dests": dest,
                "type": typ
            }

            if typ == "&":
                mod["ins"] = {}
            elif typ == "%":
                mod["on"] = False

            mods[name] = mod

    for key, mod in mods.items():
        for dest in mod["dests"]:
            if dest not in mods:
                continue

            dest_mod = mods[dest]
            if dest_mod["type"] == "&":
                dest_mod["ins"][key] = False

    counts = defaultdict(int)

    for i in range(1000):
        queue = [("broadcaster", None, False)]
        while queue:
            cur_name, src, input = queue.pop(0)
            counts[input] += 1

            if cur_name not in mods:
                continue

            cur = mods[cur_name]
            output = None

            if cur["type"] == "&":
                cur["ins"][src] = input
                output = not all(cur["ins"].values())
            elif cur["type"] == "%":
                if not input:
                    cur["on"] = not cur["on"]
                    output = cur["on"]
            elif cur["type"] is None:
                output = input

            if output is not None:
                for dest in cur["dests"]:
                    queue.append((dest, cur_name, output))

    print(counts[True] * counts[False])


if __name__ == "__main__":
    main()
