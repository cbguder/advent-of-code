#!/usr/bin/env python3


def main():
    with open('input') as f:
        lines = [line.strip() for line in f]

    algo = lines[0]
    img = lines[2:]

    for i in range(50):
        img = enhance(img, algo, i % 2)

    lit_pixels = 0
    for row in img:
        for px in row:
            if px == "#":
                lit_pixels += 1

    print(lit_pixels)


def enhance(img, algo, default=0):
    h = len(img)
    w = len(img[0])

    enhanced = []

    for y in range(-5, h + 5):
        row = ""

        for x in range(-5, w + 5):
            e_px = get_enhanced_pixel(x, y, img, algo, default)
            row += e_px

        enhanced.append(row)

    return enhanced


def get_enhanced_pixel(x, y, img, algo, default):
    n_idx = 0

    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            n_idx <<= 1
            n_idx += read_pixel(j, i, img, default)

    return algo[n_idx]


def read_pixel(x, y, img, default):
    if not 0 <= y < len(img):
        return default

    if not 0 <= x < len(img[0]):
        return default

    return int(img[y][x] == "#")


if __name__ == '__main__':
    main()
