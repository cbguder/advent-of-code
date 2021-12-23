#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from typing import List

ENERGY_MAP = {"A": 1, "B": 10, "C": 100, "D": 1000}
PODS_TO_ROOMS = {"A": 0, "B": 1, "C": 2, "D": 3}
ROOMS_TO_PODS = "ABCD"


@dataclass(frozen=True)
class Coord:
    line: int
    col: int

    @staticmethod
    def for_room_and_pos(room, pos):
        line = 3 - pos
        col = 3 + room * 2
        return Coord(line, col)

    def room_and_pos(self):
        pos = 3 - self.line
        room = int((self.col - 3) / 2)
        return room, pos


@dataclass(frozen=True)
class Move:
    src: Coord
    dst: Coord

    def steps(self):
        horiz = int(abs(self.dst.col - self.src.col))
        if horiz == 0:
            return int(abs(self.dst.line - self.src.line))

        vert = int(abs(self.src.line - 1) + abs(self.dst.line - 1))
        return horiz + vert

    def path(self):
        steps = []
        horiz_step = 1 if self.dst.col >= self.src.col else -1

        line, col = self.src.line, self.src.col

        while line > 1:
            line -= 1
            steps.append(Coord(line, col))

        while col != self.dst.col:
            col += horiz_step
            steps.append(Coord(line, col))

        while line < self.dst.line:
            line += 1
            steps.append(Coord(line, col))

        return steps


@dataclass(frozen=True)
class State:
    board: List[List[str]]

    def __repr__(self):
        lines = ["".join(line) for line in self.board]
        return "".join(lines)

    def apply_move(self, move):
        char = self.get(move.src)

        assert char in PODS_TO_ROOMS
        assert self.get(move.dst) == "."

        new_board = [line.copy() for line in self.board]
        new_board[move.dst.line][move.dst.col] = char
        new_board[move.src.line][move.src.col] = "."

        energy = move.steps() * ENERGY_MAP[char]

        return State(
            board=new_board,
        ), energy

    def get(self, coord):
        return self.board[coord.line][coord.col]

    def done(self):
        for coord in ROOM_COORDS:
            room, _ = coord.room_and_pos()
            if self.get(coord) != ROOMS_TO_PODS[room]:
                return False

        return True

    def valid_moves(self):
        valid_moves = []

        for coord in PARKING_SPOTS:
            if self.get(coord) in PODS_TO_ROOMS:
                valid_moves += self._valid_moves(coord)

        for room in range(4):
            for pos in reversed(range(2)):
                coord = Coord.for_room_and_pos(room, pos)
                if self.get(coord) in PODS_TO_ROOMS:
                    valid_moves += self._valid_moves(coord)
                    break

        return valid_moves

    def _valid_moves(self, coord):
        char = self.get(coord)
        moves = []

        if coord in ROOM_COORDS:
            room, pos = coord.room_and_pos()
            if char == ROOMS_TO_PODS[room]:
                if pos == 0:
                    return []
                else:
                    below = Coord(room, 0)
                    if self.get(below) == char:
                        return []

            for dst in PARKING_SPOTS:
                moves.append(Move(coord, dst))

        room_idx = PODS_TO_ROOMS[char]
        for pos in range(4):
            dst = Coord.for_room_and_pos(room_idx, pos)
            if self.get(dst) == '.':
                moves.append(Move(coord, dst))
                break
            elif self.get(dst) != char:
                break

        return [m for m in moves if self._is_valid_move(m)]

    def _is_valid_move(self, move):
        if self.get(move.dst) != ".":
            return False

        for coord in move.path():
            if self.get(coord) != ".":
                return False

        return True

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return hash(self) == hash(other)


PARKING_SPOTS = {
    Coord(1, 1),
    Coord(1, 2),
    Coord(1, 4),
    Coord(1, 6),
    Coord(1, 8),
    Coord(1, 10),
    Coord(1, 11),
}

ROOM_COORDS = {
    Coord(2, 3),
    Coord(3, 3),
    Coord(2, 5),
    Coord(3, 5),
    Coord(2, 7),
    Coord(3, 7),
    Coord(2, 9),
    Coord(3, 9),
}


def main():
    board = []

    with open("input") as f:
        for line in f:
            board.append([x for x in line])

    start = State(board=board)
    stack = {start}
    cheapest = {start: 0}

    min_energy = float('inf')

    while True:
        next_stack = set()

        for state in stack:
            for move in state.valid_moves():
                new_state, energy_delta = state.apply_move(move)
                new_energy = cheapest[state] + energy_delta

                if new_energy < min_energy:
                    if new_state.done():
                        min_energy = new_energy
                    elif new_state not in cheapest or cheapest[new_state] > new_energy:
                        cheapest[new_state] = new_energy
                        next_stack.add(new_state)

        if not next_stack:
            break

        stack = next_stack

    print(min_energy)


if __name__ == "__main__":
    main()
