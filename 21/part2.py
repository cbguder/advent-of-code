#!/usr/bin/env python3

from __future__ import annotations

import queue
import re
import threading
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional, List

ROLL_DIST = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@dataclass(frozen=True)
class Node:
    depth: int
    pos: List[int]
    scores: List[int]
    weight: int
    winner: Optional[int] = None


class Worker(threading.Thread):
    def __init__(self, q, win_counts, win_counts_lock):
        super().__init__()
        self.q = q
        self.win_counts = win_counts
        self.win_counts_lock = win_counts_lock

    def run(self):
        while True:
            try:
                node = self.q.get(timeout=3)
            except queue.Empty:
                return

            for roll_sum, weight in ROLL_DIST.items():
                nn = next_node(node, roll_sum, weight)
                if nn.winner is None:
                    self.q.put(nn)
                else:
                    with self.win_counts_lock:
                        self.win_counts[nn.winner] += nn.weight

            self.q.task_done()


def main():
    exp = re.compile(r"Player \d starting position: (\d+)")

    pos = []

    with open('input') as f:
        for line in f:
            m = exp.match(line)
            pos.append(int(m[1]))

    root = Node(
        depth=0,
        scores=[0, 0],
        pos=pos,
        weight=1,
    )

    win_counts = defaultdict(int)
    lock = threading.Lock()

    q = queue.Queue()
    q.put(root)
    for _ in range(8):
        Worker(q, win_counts, lock).start()

    q.join()

    print(max(win_counts.values()))


def next_node(node, roll_sum, weight):
    pos = node.pos[:]
    score = node.scores[:]

    idx = node.depth % 2
    pos[idx] += roll_sum
    while pos[idx] > 10:
        pos[idx] -= 10

    score[idx] += pos[idx]

    winner = None
    if score[idx] >= 21:
        winner = idx

    return Node(
        depth=node.depth + 1,
        pos=pos,
        scores=score,
        winner=winner,
        weight=node.weight * weight,
    )


if __name__ == '__main__':
    main()
