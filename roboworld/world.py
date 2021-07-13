
from enum import Enum
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import animation, rc
from IPython.display import HTML, display
import numpy as np
from .cellstate import CellState
from .agent import Agent


class World():
    def __init__(self, nrows, ncols, agent_position=None) -> None:
        self.stack = []
        self.ncols = ncols
        self.nrows = nrows
        self.cells = [
            [CellState.EMPTY for _ in range(ncols)] for _ in range(nrows)]

        if agent_position == None:
            agent_position = [self.nrows // 2, self.ncols // 2]
        self.agent = Agent(agent_position, self)
        self.goal = (np.random.randint(0, nrows), np.random.randint(0, ncols))
        self.objects = []

    def get_state(self, row, col):
        return self.cells[row][col]

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
               ][self.agent.position[1]] = CellState.AGENT.value
        return values

    def get_agent(self):
        return self.agent

    def push(self):
        self.stack.append(self.values())

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def get_animation(self):
        fig = plt.figure(figsize=(self.ncols, self.nrows), dpi=80)
        ax = fig.add_subplot(1, 1, 1)
        ax.grid(which='both')
        matplt = ax.matshow(
            self.values(), interpolation='nearest', vmin=0, vmax=3)
        # plt.show()

        def init():
            x_ticks = np.arange(-0.5, self.ncols+1, 1)
            y_ticks = np.arange(-0.5, self.nrows+1, 1)
            ax.grid(which='both')
            # ax.matshow(values,  interpolation ='nearest')# vmin=0, vmax=5,cmap='gray',
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_xticks(x_ticks, minor=True)
            ax.set_yticks(y_ticks, minor=True)
            ax.set_xlim(-0.5, self.ncols-0.5)
            ax.set_ylim(-0.5, self.nrows-0.5)
            return matplt,

        def update(values):
            matplt.set_data(values)
            return matplt,

        plt.close()
        anim = animation.FuncAnimation(
            fig, func=update, frames=self.stack, init_func=init, blit=True)
        return anim

    def show(self):
        fig = plt.figure(figsize=(self.ncols, self.nrows), dpi=80)
        ax = fig.add_subplot(1, 1, 1)
        x_ticks = np.arange(-0.5, self.ncols+1, 1)
        y_ticks = np.arange(-0.5, self.nrows+1, 1)
        values = self.values()
        #values = np.random.random((self.nrows, self.ncols))
        ax.grid(which='both')
        ax.matshow(values,  interpolation='nearest', vmin=0,
                   vmax=3)  # vmin=0, vmax=5,cmap='gray',
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticks(x_ticks, minor=True)
        ax.set_yticks(y_ticks, minor=True)
        ax.set_xlim(-0.5, self.ncols-0.5)
        ax.set_ylim(-0.5, self.nrows-0.5)
        return fig
