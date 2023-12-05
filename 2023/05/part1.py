#!/usr/bin/env python3


def main():
    seeds = []
    maps = []

    cur = []
    with open("input") as f:
        for line in f:
            line = line.strip()

            if not seeds:
                seeds = list(map(int, line[7:].split()))
            elif line == "":
                if cur:
                    maps.append(cur)
                    cur = []
            elif "map:" not in line:
                cur.append(list(map(int, line.split())))

    maps.append(cur)

    res = min(move1(seed, maps) for seed in seeds)
    print(res)


def move1(seed, groups):
    cur = seed

    for maps in groups:
        cur = move2(cur, maps)

    return cur


def move2(seed, maps):
    for map in maps:
        min_src = map[1]
        max_src = min_src + map[2]
        if min_src <= seed < max_src:
            offset = seed - min_src
            return map[0] + offset

    return seed


if __name__ == "__main__":
    main()
