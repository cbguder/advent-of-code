#!/usr/bin/env python3

import re

RE = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."

TEMPLATE = {
    "ore": 0,
    "clay": 0,
    "geode": 0,
    "obsidian": 0,
}

cache = {}
best = 0


def try_pay(resources, cost):
    new_resources = resources.copy()

    for resource, needed in cost.items():
        if new_resources[resource] < needed:
            return resources, False
        new_resources[resource] -= needed

    return new_resources, True


def execute(blueprint):
    resources = {
        "ore": 0,
        "clay": 0,
        "geode": 0,
        "obsidian": 0,
    }
    robots = {
        "ore": 1,
        "clay": 0,
        "geode": 0,
        "obsidian": 0,
    }
    return execute_partial(blueprint, 24, resources, robots)


def _key(h):
    return (
        h["ore"],
        h["clay"],
        h["geode"],
        h["obsidian"]
    )


def execute_partial(blueprint, minutes, resources, robots):
    global best

    cache_key = (minutes, _key(resources), _key(robots))
    if cache_key in cache:
        return cache[cache_key]

    if minutes == 0:
        return resources["geode"]

    max_geodes = 0

    bought_well = False

    for resource in ["geode", "obsidian", "clay", "ore"]:
        cost = blueprint["costs"][resource]
        new_resources, success = try_pay(resources, cost)
        if success:
            for robot_resource, count in robots.items():
                new_resources[robot_resource] += count

            new_robots = robots.copy()
            new_robots[resource] += 1

            geodes = execute_partial(blueprint, minutes - 1, new_resources, new_robots)
            max_geodes = max(max_geodes, geodes)

            if resource in {"geode", "obsidian"}:
                bought_well = True
                break

    if not bought_well or resources["ore"] <= 3:
        new_resources = resources.copy()
        for resource, count in robots.items():
            new_resources[resource] += count

        geodes = execute_partial(blueprint, minutes - 1, new_resources, robots)
        max_geodes = max(max_geodes, geodes)

    cache[cache_key] = max_geodes
    return max_geodes


def read_blueprint(line):
    m = re.match(RE, line)

    return {
        "num": int(m.group(1)),
        "costs": {
            "ore": {
                "ore": int(m.group(2))
            },
            "clay": {
                "ore": int(m.group(3))
            },
            "obsidian": {
                "ore": int(m.group(4)),
                "clay": int(m.group(5))
            },
            "geode": {
                "ore": int(m.group(6)),
                "obsidian": int(m.group(7))
            },
        }
    }


def main():
    global cache, best

    total = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            blueprint = read_blueprint(line)

            cache = {}
            best = 0

            geodes = execute(blueprint)
            print(blueprint["num"], geodes)
            total += geodes * blueprint["num"]

    print(total)


if __name__ == "__main__":
    main()
