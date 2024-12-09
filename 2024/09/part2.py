#!/usr/bin/env python3

import bisect


def main():
    with open("input") as f:
        layout = f.read().strip()

    blocks = []
    spaces = []
    pos = 0
    for i, c in enumerate(layout):
        n = int(c)

        if i % 2 == 0:
            blocks.append({
                "id": i // 2,
                "start": pos,
                "length": n,
            })
        else:
            spaces.append({
                "start": pos,
                "length": n,
            })

        pos += n

    moved_blocks = []

    while blocks:
        block = blocks.pop()

        space = None
        for i, sp in enumerate(spaces):
            if sp["start"] <= block["start"] and sp["length"] >= block["length"]:
                space = spaces.pop(i)
                break

        if space is None:
            moved_blocks.append(block)
            continue

        block["start"] = space["start"]
        moved_blocks.append(block)

        rem_length = space["length"] - block["length"]
        if rem_length > 0:
            new_space = {
                "start": space["start"] + block["length"],
                "length": rem_length
            }
            bisect.insort_left(spaces, new_space, key=lambda x: x["start"])

    ret = 0
    for bl in moved_blocks:
        i = bl["start"]
        for n in range(bl["length"]):
            ret += i * bl["id"]
            i += 1
    print(ret)


if __name__ == "__main__":
    main()
