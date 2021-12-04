#!/usr/bin/env python

def main():
    pos = 0
    depth = 0
    aim = 0

    with open('input') as f:
        for line in f:
            parts = line.split()
            n = int(parts[1])
            
            if parts[0] == 'forward':
                pos += n
                depth += aim*n
            elif parts[0] == 'down':
                aim += n
            elif parts[0] == 'up':
                aim -= n

    print(pos * depth)

if __name__ == '__main__':
    main()
