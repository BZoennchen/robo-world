# std modules
import unittest

# local modules
from roboworld import World
from roboworld import D2DVector
from roboworld.visualization import ArrayRecorder
from roboworld.visualization import MatplotVisualizer


class TestShow(unittest.TestCase):
    def test_str_to_figure(self):
        text = """N#---#---#---
-#-#-#-#-#-#-
-#-#-#-#L#-#-
-#-#-#-#L#-#-
-#-#-#-#-#-#-
---#---#O--#G"""
        world = World.str_to_world(text)
        fig = world.show(scale=0.7)
        fig.savefig('./test_show.png')
    
    def test_world_to_figure(self):
        world = World.tunnel()
        fig = world.show(scale=0.7)
        fig.savefig('./test_show_tunnel.png')


class TestAnimation(unittest.TestCase):
    def test_generate_animation(self):
        robo_position = D2DVector(4, 4)
        world = World(nrows=10, ncols=10, robo_initial_position=robo_position)
        world.add_recorder(ArrayRecorder())
        robo = world.robo
        robo.move()
        world.animate(scale=0.9, animator=lambda recorder, scale: MatplotVisualizer().animate(recorder,scale=scale, save=True, path='./test_animation.gif'))

if __name__ == '__main__':
    unittest.main()