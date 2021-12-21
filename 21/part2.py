#!/usr/bin/env python3

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Tuple, Optional

ROLL_DIST = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@dataclass(frozen=True)
class State:
    next_player: int
    pos: Tuple[int, int]
    score: Tuple[int, int]
    winner: Optional[int]


def main():
    exp = re.compile(r"Player \d starting position: (\d+)")

    pos = []

    with open('input') as f:
        for line in f:
            m = exp.match(line)
            pos.append(int(m[1]))

    start = State(
        next_player=0,
        pos=(pos[0], pos[1]),
        score=(0, 0),
        winner=None,
    )

    states = defaultdict(int)
    states[start] = 1
    prevs = defaultdict(set)

    stack = {start}
    while True:
        next_stack = set()

        for prev in stack:
            for roll_sum, weight in ROLL_DIST.items():
                next = next_state(prev, roll_sum)
                prevs[next].add((prev, weight))

                if next.winner is None:
                    next_stack.add(next)

                states[next] = sum(states[p] * w for p, w in prevs[next])

        if not next_stack:
            break

        stack = next_stack

    win_counts = defaultdict(int)
    for state, count in states.items():
        if state.winner is not None:
            win_counts[state.winner] += count

    print(max(win_counts.values()))


def next_state(prev, roll_sum):
    pos = list(prev.pos)
    score = list(prev.score)

    idx = prev.next_player
    pos[idx] += roll_sum
    while pos[idx] > 10:
        pos[idx] -= 10

    score[idx] += pos[idx]

    winner = None
    if score[idx] >= 21:
        winner = idx

    next_player = (idx + 1) % 2

    return State(
        next_player=next_player,
        pos=(pos[0], pos[1]),
        score=(score[0], score[1]),
        winner=winner
    )


if __name__ == '__main__':
    main()
