from enum import Enum
import copy
from roboworld.direction import Direction
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import animation, rc
import numpy as np
from .roboexception import InvalidWorldArgumentsExeception
from .cellstate import CellState
from .agent import Agent
import random


class World():
    def __init__(self, nrows, ncols, cells=None, agent_direction=Direction.NORTH) -> None:
        if nrows == 0 or ncols == 0 or (cells != None and (len(cells) == 0 or len(cells[0]) == 0)):
            raise InvalidWorldArgumentsExeception()
        self.stack = []
        self.ncols = ncols
        self.nrows = nrows
        if cells == None:
            self.cells = [
                [CellState.EMPTY for _ in range(ncols)] for _ in range(nrows)]
        elif nrows != len(cells) or ncols != len(cells[0]):
            raise InvalidWorldArgumentsExeception()
        else:
            self.cells = cells

        agent_position = self.__find_cell(CellState.AGENT)
        goal_position = self.__find_cell(CellState.GOAL)

        if agent_position == None:
            agent_position = [self.nrows // 2, self.ncols // 2]
        self.agent = Agent(agent_position, self,
                           agent_direction=agent_direction)

        if goal_position == None:
            while goal_position == None or (goal_position == agent_position and (ncols > 1 or nrows > 1)):
                goal_position = [np.random.randint(0, nrows),
                                 np.random.randint(0, ncols)]

        self.goal = goal_position

        self.objects = []
        self.tokens = []

        self.cells[agent_position[0]][agent_position[1]] = CellState.AGENT
        self.cells[self.goal[0]][self.goal[1]] = CellState.AGENT

        self.push()

    def is_successful(self):
        return self.agent.position == self.goal

    def get_state(self, row, col):
        return self.cells[row][col]

    def set_state(self, row, col, state):
        self.cells[row][col] = state

    def get_goal_position(self):
        return self.goal

    def is_object_at(self, row, col):
        return any([ob.position == [row, col] for ob in self.objects])

    def get_object_at(self, row, col):
        result = None
        for ob in self.objects:
            if ob.position == [row, col]:
                result = ob
                break
        if result != None:
            self.objects.remove(result)
        return result

    def set_object_at(self, row, col, ob):
        self.objects.append(ob)
        ob.set_position(row, col)

    def values(self):
        values = [[state.value for state in row] for row in self.cells]
        values[self.goal[0]][self.goal[1]] = CellState.GOAL.value
        values[self.agent.position[0]
               ][self.agent.position[1]] = CellState.AGENT.value + self.agent.headway.to_float()
        return values

    def get_agent(self):
        return self.agent

    def push(self):
        self.stack.append(self.values())

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def get_animation(self, interval=150, save=False, dpi=80):
        if len(self.stack) <= 1:
            return
        fig = plt.figure(figsize=(self.ncols, self.nrows), dpi=dpi)
        ax = fig.add_subplot(1, 1, 1)
        ax.grid(which='both')
        matplt = ax.matshow(
            self.values(), interpolation='nearest', vmin=0, vmax=3)
        x_ticks = np.arange(-0.5, self.ncols+1, 1)
        y_ticks = np.arange(-0.5, self.nrows+1, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticks(x_ticks, minor=True)
        ax.set_yticks(y_ticks, minor=True)
        ax.set_xlim(-0.5, self.ncols-0.5)
        ax.set_ylim(-0.5, self.nrows-0.5)

        i = {'index': 0}  # trick to enforce sideeffect
        stack_copy = copy.deepcopy(self.stack)

        def updatefig(*args):
            i['index'] += 1
            if i['index'] >= len(stack_copy):
                i['index'] = 0
            matplt.set_array(stack_copy[i['index']])
            return matplt,

        plt.close()
        anim = animation.FuncAnimation(
            fig, updatefig, interval=interval, blit=True, save_count=len(stack_copy))
        if save:
            anim.save('robo-world-animation.gif',
                      dpi=dpi, writer="imagemagick")
        self.stack.clear()
        self.push()
        return anim

    def show(self):
        scale = 0.5
        fig = plt.figure(figsize=(self.ncols * scale,
                         self.nrows * scale), dpi=80)
        ax = fig.add_subplot(1, 1, 1)
        x_ticks = np.arange(-0.5, self.ncols+1, 1)
        y_ticks = np.arange(-0.5, self.nrows+1, 1)
        values = self.values()
        #values = np.random.random((self.nrows, self.ncols))
        ax.grid(which='both')
        ax.matshow(values,  interpolation='nearest', vmin=0,
                   vmax=CellState.GOAL.value)  # vmin=0, vmax=5,cmap='gray',
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticks(x_ticks, minor=True)
        ax.set_yticks(y_ticks, minor=True)
        ax.set_xlim(-0.5, self.ncols-0.5)
        ax.set_ylim(-0.5, self.nrows-0.5)
        plt.close()
        return fig

    def __find_cell(self, cellstate):
        for i, col in enumerate(self.cells):
            for j, state in enumerate(col):
                if state == cellstate:
                    return [i, j]
        return None

    @staticmethod
    def corridor(length=10):
        cells = [[CellState.AGENT] +
                 [CellState.EMPTY for _ in range(length-2)] + [CellState.GOAL]]
        return World(nrows=len(cells), ncols=len(cells[0]), cells=cells, agent_direction=Direction.EAST)

    @staticmethod
    def maze():
        text = """N#---#---#---
-#-#-#-#-#-#-
-#-#-#-#-#-#-
-#-#-#-#-#-#-
-#-#-#-#-#-#-
---#---#---#G"""
        return World.str_to_world(text)

    @staticmethod
    def str_to_world(text):
        cells = []
        agent_direction = Direction.EAST
        for row, line in enumerate(text.splitlines()):
            cells.append([])
            for c in line:
                if c in ['N', 'S', 'E', 'W', 'R']:
                    state = CellState.AGENT
                    if c == 'N':
                        agent_direction = Direction.NORTH
                    elif c == 'S':
                        agent_direction = Direction.SOUTH
                    elif c == 'W':
                        agent_direction = Direction.WEST
                    elif c == 'W':
                        agent_direction = Direction.EAST
                    else:
                        agent_direction = random.choice(
                            [Direction.NORTH, Direction.SOUTH, Direction.WEST, Direction.EAST])
                elif c == '#':
                    state = CellState.OBSTACLE
                elif c == 'G':
                    state = CellState.GOAL
                else:
                    state = CellState.EMPTY
                cells[row].append(state)
        return World(nrows=len(cells), ncols=len(cells[0]), cells=cells, agent_direction=agent_direction)