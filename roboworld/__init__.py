__version__ = '0.1.2'
__author__ = 'Benedikt Zoennchen'

from .roboworld import World
from .visualization import ArrayRecorder
from .vector import D2DVector

from IPython.display import HTML, display

def animate(world: World):
    anim = world.animate()
    if anim != None:
        display(HTML(anim.to_jshtml()))

def corridor(length=10, random_headway=False, nobjects=0):
    world =  World.corridor(length=length, random_headway=random_headway, nstones=nobjects)
    world.add_recorder(ArrayRecorder())
    return world

def simple_tunnel(tunnel_length:int=4, length:int=8):
    world =  World.simple_tunnel(tunnel_length, length)
    world.add_recorder(ArrayRecorder())
    return world

def maze():
    world = World.maze()
    world.add_recorder(ArrayRecorder())
    return world

def str_to_world(text):
    world = World.str_to_world(text)
    world.add_recorder(ArrayRecorder())
    return world

def new_world(nrows=5, ncols=9, robo_position=None, goal_position=None):
    world = World(nrows=nrows, ncols=ncols, robo_initial_position=robo_position, goal_position=goal_position)
    world.add_recorder(ArrayRecorder())
    return world

def complex_maze(nrows=10, ncols=10, robo_direction=None):
    world = World.complex_maze(nrows=nrows, ncols=ncols, robo_direction=robo_direction)
    world.add_recorder(ArrayRecorder())
    return world