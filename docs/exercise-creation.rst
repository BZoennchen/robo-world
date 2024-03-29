Create an Exercise
==================

Teachers can define their exercises by 

1. chose/create a suitable ``World``
2. and define the challenge for it. 

Chose a World
-------------

In general, one can distinguish between 

Solving a problem instance
    If the world creation is not randomized, one might want to allow students to solve a specific problem.
    They look at the ``World`` and move ``Robo`` accordingly.
    Therefore, they do not rely on **loops**.

Solving a set of problems
    If the world creation is or can be randomized, one might want to force students to solve a whole set of problems.
    For example, navigate ``Robo`` through a randomized maze (generated by ``complex_maze()``)

There are a lot of predefined worlds that can be the basis for the teacher's exercises.
Use the following factory functions to make use of them.
To do call

>>> import roboworld as rw
>>> world = rw.factory_function(...)
>>> ...

Beginners
~~~~~~~~~~~~~~~~~~~~

These ``Worlds`` can be the basis for learning the concept of **method calls** and **conditionals**.
If one uses fixed dimensions of the ``World``, students can solve those puzzles without using **loops**.

.. autofunction:: roboworld.leaf_corridor

**Example exercise:** Move ``Robo``from left to right. You will encounter LEAFS (green) along the way. Pick up all the LEAFS!

**Challenge:** Students have to move ``Robo``, test for LEAFS and pick them up.

.. image:: ./_static/figs/world-leaf-corridor.png

.. autofunction:: roboworld.corridor

**Example exercise:** Move ``Robo``from left to right. You will encounter STONES (orange) along the way. ``Robo`` can only carry one STONE at a time.

**Challenge:** Students have to move ``Robo``, test for STONES, pick them up and put them down again. Therefore, they also have to turn ``Robo`` multiple times.

.. image:: ./_static/figs/world-corridor.png

.. autofunction:: roboworld.new_world

**Example exercise:** Move ``Robo`` (blue) to its goal (purple).

**Challenge:** Students have to move ``Robo``. If the ``World`` is randomized (e.g., random goal position), students have to come up with a **search strategy**!

.. image:: ./_static/figs/world-new-world.png

.. autofunction:: roboworld.tunnel

**Example exercise:** Move ``Robo`` (blue) to the tunnel exit (purple) (or entry) without using ``robo.is_at_goal()``.

**Challenge:** Students have to define the tunnel exit and entry (the wall on the left and right) and test for it while walking towards the WEST.

.. image:: ./_static/figs/world-tunnel.png

Intermediates
~~~~~~~~~~~~~~~~~~~~

The next set of ``Worlds`` can be used to introduce **loops**.

.. autofunction:: roboworld.simple_slalom

**Example exercise:** Move ``Robo`` (blue) to its goal by passing all WALLS (dark grey) from NORTH to SOUTH or vice versa, i.e., walk a slalom!

**Challenge:** Students have to generate a slalom movement pattern using multiple left turns and move instructions.

.. image:: ./_static/figs/world-simple-slalom.png

.. autofunction:: roboworld.multi_slalom

**Example exercise:** Move ``Robo`` (blue) to its goal by passing all WALLS (dark grey) from NORTH to SOUTH or vice versa, i.e., walk a slalom!

**Challenge:** Students have to generate a slalom movement pattern using multiple left turns and move instructions.

.. image:: ./_static/figs/world-multi-slalom.png

.. autofunction:: roboworld.round_trip

**Example exercise:** Move ``Robo`` (blue) to its goal. Find and pick up all the LEAFS!

**Challenge:** Students have to generate round-trip movement patterns using multiple left turns and move instructions. They have to test for LEAFS and pick them up. They should abstract new instructions: 

+ move ``Robo`` through a right corner
+ move ``Robo`` through a left corner

.. image:: ./_static/figs/world-round-trip.png

.. autofunction:: roboworld.maze

**Example exercise:** Move ``Robo`` (blue) to its goal.

**Challenge:** Students have to recognize that the required movement pattern is repetitive and use this to their advantage.

.. image:: ./_static/figs/world-maze.png

.. autofunction:: roboworld.leaf_cross

**Example exercise:** Move ``Robo`` (blue) to its goal. Invert all cells, i.e., if there is no LEAF at a cell, place one. If there is a LEAF at a cell, remove it!

**Challenge:** Students have to move ``Robo`` through the whole ``World``, test for LEAFS, and invert the cells' state accordingly.
If ``Robo`` is initialized with enough LEAFS, the exercise is easier because students do not have to worry about visiting too many EMPTY cells consecutively.

.. image:: ./_static/figs/world-leaf-cross.png

.. autofunction:: roboworld.pacman

**Example exercise:** Move ``Robo`` (blue) to its goal by following the path of LEAFS. 

**Challenge:** Students have to move ``Robo`` in a zig-zag movement pattern while ``Robo`` sensors the LEAFS accordingly.

.. image:: ./_static/figs/world-pacman.png

Experts
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: roboworld.complex_maze

**Example exercise 1:** Move ``Robo`` (blue) through a **randomly** generated maze to its goal (purple).

**Example exercise 2:** Let ``Robo`` (blue) compute the shortest path through the **randomly** generated maze to its goal (purple). 
After computation, move the ``Robo`` back to its starting position and walk directly to its goal using the computed shortest path.

**Challenge 1:** Students have to develop a **dept-first search strategy**.

**Challenge 2:** Students must develop a **breath-first search strategy**, a way to move 'backward' and repeat a specific walk.

*Hint:* The `dept-first <https://en.wikipedia.org/wiki/Depth-first_search>`_ search can be used to develop a `breath-first search <https://en.wikipedia.org/wiki/Breadth-first_search>`_ strategy.

.. image:: ./_static/figs/world-complex-maze.png

.. autofunction:: roboworld.game_of_life

**Example exercise:** Let ``Robo`` play Conway's Game of Life. 
Update all cells according to the rules by manipulating the ``World`` using ``Robo``.

**Challenge:** Students have to understand the rules of Conway's Game of Life. 
They have to develop a strategy such that the parallel update character of the cells is not broken.

*Hints:* ``Robo`` has enough LEAFS. 
Put a LEAF on each cell. 
``Robo`` can ``mark`` and ``unmark`` a cell, this might be useful.

.. image:: ./_static/figs/world-game-of-life.png

.. autofunction:: roboworld.sorting

**Example exercise:** Let ``Robo`` sort the LEAF-rows of the ``World``. 
The consecutive LEAFS of each row of the ``World`` represent a number.
Bring these rows/numbers from bottom to top in ascending order.

**Challenge:** Students understand and implement some sorting algorithms (e.g., `bubble sort <https://en.wikipedia.org/wiki/Bubble_sort>`_ ).
They have to abstract ``Robo`` instructions in such a way that they can make use of their sorting algorithm.

.. image:: ./_static/figs/world-sorting.png


Create Your Own World
--------------------------

The easiest way to construct a customized ``World`` is to use yet another factory function.

.. autofunction:: roboworld.str_to_world

The string representation ``text`` has to be a rectangular string, i.e., a multiline string for which each line has the same length.
Furthermore, if there is no ``'G'`` (for the goal position), it will be placed at a random EMPTY position. 
If there is no ``'R'``, ``'N'``, ``'W'``, ``'S'`` or ``'E'`` the robot will be placed at the center of the ``World``; this might be impossible thus causes an exception!

For example:

>>> import roboworld
>>> text= """############
>>> #----LL----#
>>> #----------#
>>> #----R-----#
>>> #-O--------#"""
>>>
>>> world = rw.str_to_world(text)
>>> fig = world.show(scale=0.3)
>>> fig.savefig('world-str-to-world.png')

gives us 

.. image:: ./_static/figs/world-str-to-world.png

Note that the image is mirrored because position ``(0, 0)`` is at the **top** left.

Define the Challenge
--------------------------

Above we already propose some challenges, but one is free to define a new one.
Your challenges will likely depend on each other.
For example, in one challenge, students might have to define a function to turn ``Robo`` by 180 degrees - a very useful abstraction.
This function will certainly be very helpful in solving many other problems.

An example stream of challenges can be found `here <https://bzoennchen.github.io/ct-book/chapters/04/robo-world.html>`_.
The text is written in German.