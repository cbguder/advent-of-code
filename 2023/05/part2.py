#!/usr/bin/env python3


def main():
    seeds = []
    groups = []

    cur = []
    with open("input") as f:
        for line in f:
            line = line.strip()

            if not seeds:
                seeds = list(map(int, line[7:].split()))
            elif line == "":
                if cur:
                    cur.sort(key=lambda x: x[1])
                    groups.append(cur)
                    cur = []
            elif "map:" not in line:
                cur.append(list(map(int, line.split())))

    cur.sort(key=lambda x: x[1])
    groups.append(cur)

    mins = []

    for i in range(len(seeds) // 2):
        min_src = seeds[i*2]
        max_src = min_src + seeds[i*2 + 1]

        rng = (min_src, max_src)
        moved = move1(rng, groups)
        moved.sort(key=lambda x: x[0])
        mins.append(moved[0][0])

    print(min(mins))


def move1(rng, groups):
    cur = [rng]

    for maps in groups:
        cur = move2(cur, maps)

    return cur


def move2(ranges, maps):
    ret = []

    for rng in ranges:
        ret += move3(rng, maps)

    return ret


def move3(rng, maps):
    rem = rng
    ret = []

    for map in maps:
        if not rem:
            break
        r2, rem = move4(rem, map)
        if r2 is not None:
            ret.append(r2)

    if rem:
        ret.append(rem)
    return ret


def move4(rng, map):
    rng_min, rng_max = rng
    map_src_min, map_src_max = map[1], map[1] + map[2]

    if rng_max < map_src_min:
        return None, rng
    elif rng_min >= map_src_max:
        return None, rng

    overlap_min = max(rng_min, map_src_min)
    overlap_max = min(rng_max, map_src_max)

    map_dst_min, map_dst_max = map[0], map[0] + map[2]
    mapped_min = map_dst_min + (overlap_min - map_src_min)
    mapped_max = map_dst_min + (overlap_max - map_src_min)
    mapped = (mapped_min, mapped_max)

    rem = None
    if overlap_min > rng_min:
        rem = (rng_min, overlap_min)
    elif overlap_max < rng_max:
        rem = (overlap_max, rng_max)

    return mapped, rem


if __name__ == "__main__":
    main()
