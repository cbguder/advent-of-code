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

    while True:
        if spaces[0]["start"] >= blocks[-1]["start"]:
            break

        space = spaces.pop(0)
        block = blocks.pop()

        if space["length"] >= block["length"]:
            new_block = dict(block)
            new_block["start"] = space["start"]
            bisect.insort_left(blocks, new_block, key=lambda x: x["start"])

            rem_length = space["length"] - block["length"]
            if rem_length > 0:
                new_space = {
                    "start": space["start"] + block["length"],
                    "length": rem_length
                }
                spaces.insert(0, new_space)
        else:
            bl1 = dict(block)
            bl1["start"] = space["start"]
            bl1["length"] = space["length"]
            bisect.insort_left(blocks, bl1, key=lambda x: x["start"])

            bl2 = dict(block)
            bl2["length"] = block["length"] - space["length"]
            blocks.append(bl2)

    ret = 0
    for bl in blocks:
        i = bl["start"]
        for n in range(bl["length"]):
            ret += i * bl["id"]
            i += 1
    print(ret)


if __name__ == "__main__":
    main()
