#!/usr/bin/env python3


def main():
    with open("input") as f:
        input = f.readline().strip()

    xr, yr = input[13:].split(", ")
    xmin, xmax = tuple(map(int, xr[2:].split("..")))
    ymin, ymax = tuple(map(int, yr[2:].split("..")))

    res = find_highest_y(xmin, xmax, ymin, ymax)
    print(res)


def find_highest_y(xmin, xmax, ymin, ymax):
    highest = None

    vx = 1
    while True:
        highest_with_vx = find_highest_y_with_vx(vx, xmin, xmax, ymin, ymax)
        if highest_with_vx is None:
            if highest is not None:
                break
        elif highest is None or highest_with_vx > highest:
            highest = highest_with_vx
        vx += 1

    return highest


def find_highest_y_with_vx(vx, xmin, xmax, ymin, ymax):
    highest = None

    vy = 0
    nones = 0
    while True:
        highest_with_v = find_highest_y_with_velocity(vx, vy, xmin, xmax, ymin, ymax)

        if highest_with_v is not None:
            if highest is None or highest_with_v > highest:
                highest = highest_with_v
        else:
            nones += 1
            if nones > 15:
                break

        vy += 1

    return highest


def find_highest_y_with_velocity(vx, vy, xmin, xmax, ymin, ymax):
    highest = 0

    x, y = 0, 0
    while True:
        x, y, vx, vy = step(x, y, vx, vy)
        if y > highest:
            highest = y

        if xmin <= x <= xmax and ymin <= y <= ymax:
            break

        if x > xmax or y < ymin:
            return None

    return highest


def step(x, y, vx, vy):
    x += vx
    y += vy

    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1

    vy -= 1

    return x, y, vx, vy


if __name__ == '__main__':
    main()
