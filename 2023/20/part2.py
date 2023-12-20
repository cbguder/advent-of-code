#!/usr/bin/env python3

from copy import deepcopy
from math import lcm


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

    rx_inputs_1 = [k for k, v in mods.items() if "rx" in v["dests"]]
    assert len(rx_inputs_1) == 1
    rx_inputs_2 = set(k for k, v in mods.items() if rx_inputs_1[0] in v["dests"])

    networks = []

    for src in mods["broadcaster"]["dests"]:
        network = set()
        queue = [src]
        while queue:
            cur = queue.pop(0)
            if cur in network:
                continue

            network.add(cur)
            if cur in mods:
                queue.extend(mods[cur]["dests"])

        dest = network & rx_inputs_2
        assert len(dest) == 1
        networks.append((src, network, list(dest)[0]))

    loops = []

    for src, net, dest in networks:
        reset_mods = deepcopy(mods)
        reset_mods = {
            k: v
            for k, v in reset_mods.items()
            if k in net | {"broadcaster"}
        }

        i = 1
        while True:
            done = run(reset_mods, dest)
            if done:
                loops.append(i)
                break
            i += 1

    print(lcm(*loops))


def run(mods, end):
    queue = [("broadcaster", None, False)]
    while queue:
        cur_name, src, input = queue.pop(0)

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
                if not output and dest == end:
                    return True
                queue.append((dest, cur_name, output))

    return False


if __name__ == "__main__":
    main()
