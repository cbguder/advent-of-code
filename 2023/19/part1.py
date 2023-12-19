#!/usr/bin/env python3
import re


def main():
    flows = {}
    flows_done = False
    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()

            if line == "":
                flows_done = True
            elif not flows_done:
                m = re.match(r"(\w+)\{(.+)}", line)
                label, raw_flow = m.groups()
                parts1 = raw_flow.split(",")
                parts2 = [p.split(":") for p in parts1]
                for i in range(len(parts2)):
                    if len(parts2[i]) > 1:
                        s = re.split(r"([<>])", parts2[i][0])
                        parts2[i] = s + [parts2[i][-1]]
                flows[label] = parts2
            else:
                parts1 = line[1:-1].split(",")
                parts2 = [p.split("=") for p in parts1]
                part = {k: int(v) for k, v in parts2}
                dest = process(flows, part)

                if dest == "A":
                    ret += sum(part.values())

    print(ret)


def process(flows, part):
    cur = "in"
    while cur not in {"R", "A"}:
        cur = process_single(flows[cur], part)
    return cur


def process_single(flow, part):
    for step in flow:
        if len(step) == 1:
            return step[0]
        elif step[1] == "<":
            if part[step[0]] < int(step[2]):
                return step[3]
        elif step[1] == ">":
            if part[step[0]] > int(step[2]):
                return step[3]
        else:
            assert False


if __name__ == "__main__":
    main()
