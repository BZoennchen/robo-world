from .cellstate import CellState
from .direction import Direction


class Agent():
    def __init__(self, position, world) -> None:
        self.world = world
        self.position = position

    def is_reachable(self, direction):
        y, x = self.position
        if direction == Direction.LEFT:
            return x-1 >= 0 and self.world.get_state(y, x-1) != CellState.OBSTACLE
        elif direction == Direction.RIGHT:
            return x+1 < self.world.ncols and self.world.get_state(y, x+1) != CellState.OBSTACLE
        elif direction == Direction.UP:
            return y+1 < self.world.nrows and self.world.get_state(y+1, x) != CellState.OBSTACLE
        elif direction == Direction.DOWN:
            return y-1 >= 0 and self.world.get_state(y-1, x) != CellState.OBSTACLE

    def can_move_left(self):
        return self.is_reachable(Direction.LEFT)

    def can_move_right(self):
        return self.is_reachable(Direction.RIGHT)

    def can_move_up(self):
        return self.is_reachable(Direction.UP)

    def can_move_down(self):
        return self.is_reachable(Direction.DOWN)

    def move_left(self):
        if self.can_move_left():
            self.position[1] -= 1
        self.world.push()

    def move_right(self):
        if self.can_move_right():
            self.position[1] += 1
        self.world.push()

    def move_up(self):
        if self.can_move_up():
            self.position[0] += 1
        self.world.push()

    def move_down(self):
        if self.can_move_down():
            self.position[0] -= 1
        self.world.push()

    def reached_goal(self):
        return self.position[0] == self.world.goal[0] and self.position[1] == self.world.goal[1]
