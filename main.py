"""Testing figure and animation creation

This script is for testing purposes.

"""

import roboworld

def generate_test_fig1():
    text = """N#---#---#---
-#-#-#-#-#-#-
-#-#-#-#L#-#-
-#-#-#-#L#-#-
-#-#-#-#-#-#-
---#---#O--#G"""
    world = World.str_to_world(text)
    fig = world.show(scale=0.7)
    fig.savefig('./asserts/test_show.png')

def generate_test_fig2():
    world = World.simple_tunnel()
    fig = world.show(scale=0.7)
    fig.savefig('./asserts/test_show_tunnel.png')

def generate_test_animation1():
    robo_position = D2DVector(4, 4)
    world = World(nrows=10, ncols=10, robo_initial_position=robo_position)
    world.add_recorder(ArrayRecorder())
    robo = world.robo
    robo.move()
    world.animate(scale=0.9, animator=lambda recorder, scale: MatplotVisualizer().animate(recorder,scale=scale, save=True, path='./asserts/test_animation.gif'))

if __name__ == "__main__":
    generate_test_fig1()
    generate_test_fig2()
    generate_test_animation1()