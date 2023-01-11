# std modules
import random
import unittest
import roboworld
from roboworld.visualization import MatplotVisualizer

# local modules
from roboworld.world import CellState
from roboworld.world import Orientation
from roboworld.world import CellOccupiedException, LeafMissingException, SpaceIsEmptyException, SpaceIsFullException, StoneInFrontException, StoneMissingException, World
from roboworld.vector import D2DVector

def create_wall_corridor():
    text = "E-#G"
    world = World.str_to_world(text)
    robo = world.robo
    return world, robo

def create_empty_corridor():
    text = "E----G"
    world = World.str_to_world(text)
    robo = world.robo
    return world, robo

def create_leaf_corridor():
    text = "ELLLLLG"
    world = World.str_to_world(text)
    robo = world.robo
    return world, robo

def create_stone_corridor():
    text = "E-O-G"
    world = World.str_to_world(text)
    robo = world.robo
    return world, robo

class TestMove(unittest.TestCase):
    def test(self):
        _, robo = create_empty_corridor()
        self.assertEqual(robo.position, D2DVector(0, 0))
        robo.move()
        self.assertEqual(robo.position, D2DVector(0, 1))
        
class TestWall(unittest.TestCase):
    def test(self):
        _, robo = create_wall_corridor()
        self.assertFalse(robo.is_wall_in_front())
        robo.turn_left()
        self.assertTrue(robo.is_wall_in_front())
        robo.turn_left()
        self.assertTrue(robo.is_wall_in_front())
        robo.turn_left()
        self.assertTrue(robo.is_wall_in_front())
        robo.turn_left()
        self.assertFalse(robo.is_wall_in_front())
        robo.move()
        self.assertTrue(robo.is_wall_in_front())

class TestTurnLeft(unittest.TestCase):
    def test(self):
        _, robo = create_empty_corridor()
        self.assertEqual(robo._robo.orientation, Orientation.EAST)
        robo.turn_left()
        self.assertEqual(robo._robo.orientation, Orientation.NORTH)
        robo.turn_left()
        self.assertEqual(robo._robo.orientation, Orientation.WEST)
        robo.turn_left()
        self.assertEqual(robo._robo.orientation, Orientation.SOUTH)
        robo.turn_left()
        self.assertEqual(robo._robo.orientation, Orientation.EAST)
    
class TestTakeLeafs(unittest.TestCase):
    def test(self):
        _, robo = create_leaf_corridor()
        self.assertEqual(robo._robo.nleafs, 0)
        self.assertFalse(robo._robo.is_carrying_leafs())
        self.assertFalse(robo.is_carrying_leafs())
        self.assertTrue(robo.is_leaf_in_front())
        
        with self.assertRaises(LeafMissingException):
            robo.take_leaf()
        
        robo.move()
        self.assertTrue(robo.is_leaf_in_front())
        robo.take_leaf()
        self.assertEqual(robo._robo.nleafs, 1)
        self.assertTrue(robo.is_carrying_leafs())
        robo.move()
        robo.take_leaf()
        self.assertEqual(robo._robo.nleafs, 2)
        self.assertEqual(robo._robo.grid._get_state(*robo.position), CellState.EMPTY)
        robo.put_leaf()
        self.assertEqual(robo._robo.nleafs, 1)
        self.assertEqual(robo._robo.grid._get_state(*robo.position), CellState.LEAF)
        
        with self.assertRaises(CellOccupiedException):
            robo.put_leaf()

class TestIsInFrontEndOfWorld(unittest.TestCase):
    def test(self):
        _, robo = create_empty_corridor()
        for _ in range(5):
            robo.move()
        self.assertTrue(robo.is_at_goal())
        self.assertFalse(robo.is_leaf_in_front())
        self.assertFalse(robo.is_stone_in_front())
        self.assertFalse(robo.is_mark_in_front())
        self.assertTrue(robo.is_wall_in_front())
        

class TestTakeStone(unittest.TestCase):
    def test(self):
        _, robo = create_stone_corridor()
        self.assertFalse(robo.is_carrying_stone())
        self.assertFalse(robo.is_stone_in_front())
        
        with self.assertRaises(SpaceIsEmptyException):
            robo.put_stone_in_front()
        
        with self.assertRaises(StoneMissingException):
            robo.take_stone_in_front()
        
        robo.move()
        
        with self.assertRaises(StoneInFrontException):
            robo.move()
            
        self.assertTrue(robo.is_stone_in_front())
        robo.take_stone_in_front()
        
        with self.assertRaises(SpaceIsFullException):
            robo.take_stone_in_front()
        
        robo.put_stone_in_front()
               
class TestMarking(unittest.TestCase):
    def test(self):
        world = World(5, 5)
        robo = world.robo
        self.assertFalse(robo.is_mark_in_front())
        robo.set_mark()
        robo.move()
        robo.turn_left()
        robo.turn_left()
        self.assertTrue(robo.is_mark_in_front())

class TestRandomWalk(unittest.TestCase):
    def test(self):
        robo_position = D2DVector(4, 4)
        world = World(nrows=10, ncols=10, robo_initial_position=robo_position)
        robo = world.robo

        while not robo.is_at_goal():
            turns = random.choice([0, 1, 2, 3])
            for _ in range(turns):
                robo.turn_left()
            if not robo.is_wall_in_front():
                robo_position = robo.move()
        self.assertEqual(robo_position, world._grid.goal_position, f'{robo_position} != {world._grid.goal_position}')
        
class Test3Right1Up(unittest.TestCase):
    def test(self):
        robo_position = D2DVector(4, 4)
        world = World(nrows=10, ncols=10, robo_initial_position=robo_position)
        robo = world._robo

        robo._Robo__move_east()
        robo._Robo__move_east()
        robo._Robo__move_east()
        robo._Robo__move_north()
        robo._Robo__move_north()
        robo_position = robo._Robo__move_north()
        self.assertEqual(robo_position, D2DVector(7, 7), f'{robo_position} != {D2DVector(7, 7)}')
      
class TestDeterministicWalk(unittest.TestCase):
    def test(self):
        def walk_to_wall(robo, condition = lambda robo: True):
            while not robo.is_wall_in_front() and condition(robo):
                robo.move()

        def turn(robo):
            robo.turn_left()
            robo.turn_left()
        
        def turn_north(robo):
            while not robo.is_facing_north():
                robo.turn_left()

        def turn_west(robo):
            turn_north(robo)
            robo.turn_left()

        def turn_south(robo):
            turn_north(robo)
            turn(robo)

        def turn_east(robo):
            turn_west(robo)
            turn(robo)
            
        def walk_west(robo, condition = lambda robo: True):
            turn_west(robo)
            walk_to_wall(robo, condition)
            
        def walk_north(robo, condition = lambda robo: True):
            turn_north(robo)
            walk_to_wall(robo, condition)

        def walk_south(robo, condition = lambda robo: True):
            turn_south(robo)
            walk_to_wall(robo, condition)
            
        def walk_north_west(robo, condition = lambda robo: True):
            walk_west(robo, condition)
            walk_north(robo, condition)

        def determined_walk(robo):
            condition = lambda robo: not robo.is_at_goal()
            
            walk_north_west(robo, condition)
                
            down = True
            while not robo.is_at_goal():
                if down:
                    walk_south(robo, condition)
                else:
                    walk_north(robo, condition)
                turn_east(robo)
                if not robo.is_at_goal() and not robo.is_wall_in_front():
                    robo.move()
                down = not down  
                
        nrows = 11
        ncols = 11
        world = roboworld.new_world(nrows=nrows, ncols=ncols)
        robo = world.robo
        determined_walk(robo)
        self.assertTrue(robo.is_at_goal())
        
if __name__ == '__main__':
    unittest.main()