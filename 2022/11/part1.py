#!/usr/bin/env python3


def apply_operation(item, op):
    assert op[0] == "old"
    if op[2] == "old":
        term = item
    else:
        term = int(op[2])

    if op[1] == "+":
        res = item + term
    elif op[1] == "*":
        res = item * term
    else:
        assert False

    return res // 3


def target(new, monkey):
    if new % monkey["modulo"] == 0:
        return monkey["true"]
    return monkey["false"]


def main():
    monkeys = []

    with open("input") as f:
        monkey = None

        for line in f:
            line = line.strip()
            if line.startswith("Monkey"):
                monkey = {"inspections": 0}
                monkeys.append(monkey)
            elif line.startswith("Starting items:"):
                monkey["items"] = list(map(int, line[16:].split(", ")))
            elif line.startswith("Operation: new ="):
                monkey["operation"] = line[17:].split()
            elif line.startswith("Test: divisible by"):
                monkey["modulo"] = int(line[19:])
            elif line.startswith("If true: throw to monkey"):
                monkey["true"] = int(line[25:])
            elif line.startswith("If false: throw to monkey"):
                monkey["false"] = int(line[25:])

    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            monkey["inspections"] += len(monkey["items"])
            for item in monkey["items"]:
                new = apply_operation(item, monkey["operation"])
                dest = target(new, monkey)
                monkeys[dest]["items"].append(new)
            monkey["items"] = []

    insps = [m["inspections"] for m in monkeys]
    top = sorted(insps, reverse=True)[:2]

    print(top[0] * top[1])


if __name__ == "__main__":
    main()
