#!/usr/bin/env python3


def dir_size(directory):
    size = 0

    for name, size_or_children in directory.items():
        if isinstance(size_or_children, dict):
            size += dir_size(size_or_children)
        else:
            size += size_or_children

    return size


def all_dir_sizes(root):
    for name, size_or_children in root.items():
        if isinstance(size_or_children, dict):
            yield dir_size(size_or_children)

            for size in all_dir_sizes(size_or_children):
                yield size


def main():
    root = {}
    path = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            if line == "$ cd /":
                pass
            elif line == "$ ls":
                pass
            elif line.startswith("$ cd"):
                dirname = line.split()[2]
                if dirname == "..":
                    path.pop()
                else:
                    path.append(dirname)
            else:
                current = root
                for part in path:
                    current = current[part]

                size, name = line.split()
                if size == "dir":
                    current[name] = {}
                else:
                    current[name] = int(size)

    total = 0

    for size in all_dir_sizes(root):
        if size <= 100000:
            total += size

    print(total)


if __name__ == "__main__":
    main()
