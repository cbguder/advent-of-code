#!/usr/bin/env python3


def main():
    with open("input") as f:
        input = f.readline().strip()

    xr, yr = input[13:].split(", ")
    xmin, xmax = tuple(map(int, xr[2:].split("..")))
    ymin, ymax = tuple(map(int, yr[2:].split("..")))

    vels = find_valid_velocities(xmin, xmax, ymin, ymax)
    print(len(vels))


def find_valid_velocities(xmin, xmax, ymin, ymax):
    valid_velocities = set()

    vx = 1
    while True:
        velocities = find_valid_velocities_with_vx(vx, xmin, xmax, ymin, ymax)
        valid_velocities.update(velocities)
        vx += 1

        if vx > xmax:
            break

    return valid_velocities


def find_valid_velocities_with_vx(vx, xmin, xmax, ymin, ymax):
    valid_velocities = set()
    misses = 0

    vy = ymin
    while True:
        if lands_in_target(vx, vy, xmin, xmax, ymin, ymax):
            valid_velocities.add((vx, vy))
        else:
            misses += 1
            if misses > 200:
                break

        vy += 1

    return valid_velocities


def lands_in_target(vx, vy, xmin, xmax, ymin, ymax):
    x, y = 0, 0
    while True:
        x, y, vx, vy = step(x, y, vx, vy)

        if xmin <= x <= xmax and ymin <= y <= ymax:
            return True

        if vx == 0 and x < xmin:
            return False

        if x > xmax or y < ymin:
            return False


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
