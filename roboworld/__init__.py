__version__ = '0.0.1'

from .agent import Agent
from .world import World
from IPython.display import HTML, display


def animate(world):
    anim = world.get_animation(save=True)
    if anim != None:
        display(HTML(anim.to_jshtml()))


def corridor(length=10, random_headway=False, nobjects=0):
    return World.corridor(length=length, random_headway=random_headway, nobjects=nobjects)


def maze():
    return World.maze()


def str_to_world(text):
    return World.str_to_world(text)


def new_world(nrows=5, ncols=9):
    return World(nrows=nrows, ncols=ncols)
