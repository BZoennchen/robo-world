from enum import Enum


class CellState(Enum):
    EMPTY = 0
    OBSTACLE = 1
    AGENT = 2
    GOAL = 3
