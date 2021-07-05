
from enum import Enum
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import animation, rc
from IPython.display import HTML, display
import numpy as np
from .cellstate import CellState
from .agent import Agent


class World():
    def __init__(self, nrows, ncols) -> None:
        self.stack = []
        self.ncols = ncols
        self.nrows = nrows
        self.cells = [
            [CellState.EMPTY for _ in range(ncols)] for _ in range(nrows)]
        self.agent = Agent([self.nrows // 2, self.ncols // 2], self)
        self.goal = (np.random.randint(0, nrows), np.random.randint(0, ncols))

    def get_state(self, row, col):
        return self.cells[row][col]

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
