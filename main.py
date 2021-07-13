from roboworld.world import World
from roboworld.agent import Agent
from roboworld.direction import Direction

import random


def threeRightAndUp():
    agent_position = [4, 4]
    world = World(nrows=10, ncols=10, agent_position=agent_position)
    agent = world.get_agent()

    agent._Agent__move_east()
    agent._Agent__move_east()
    agent._Agent__move_east()
    agent._Agent__move_north()
    agent._Agent__move_north()
    agent_position = agent._Agent__move_north()
    assert agent_position == [7, 7], f'{agent_position} != {[7, 7]}'
    #anim = world.get_animation()
    #anim.save('./asserts/steps.gif', writer='imagemagick')


def randomWalk():
    agent_position = [4, 4]
    world = World(nrows=10, ncols=10, agent_position=agent_position)
    agent = world.get_agent()

    while not agent.is_at_goal():
        turns = random.choice([0, 1, 2, 3])
        for _ in range(turns):
            agent.turn_left()
        if not agent.is_wall_in_front():
            agent_position = agent.move()
    goal_position = [world.get_goal_position()[0],
                     world.get_goal_position()[1]]
    assert agent_position == goal_position, f'{agent_position} != {goal_position}'


def deterministicWalk():
    agent_position = [4, 4]
    world = World(nrows=10, ncols=10, agent_position=agent_position)
    agent = world.get_agent()

    agent._Agent__turn_to_west()
    assert agent._Agent__get_direction() == Direction.WEST
    while not agent.is_at_goal() and not agent.is_wall_in_front():
        agent_position = agent.move()

    agent._Agent__turn_to_north()
    assert agent._Agent__get_direction() == Direction.NORTH
    while not agent.is_at_goal() and not agent.is_wall_in_front():
        agent_position = agent.move()

    assert agent_position == [9, 0]
    agent._Agent__turn()
    assert agent._Agent__get_direction() == Direction.SOUTH

    while not agent.is_at_goal():
        # (1) move down
        while not agent.is_at_goal() and not agent.is_wall_in_front():
            agent_position = agent.move()  # move down / south

        # (2) move one step right
        agent.turn_left()
        if not agent.is_wall_in_front():
            assert agent._Agent__get_direction() == Direction.EAST
            if not agent.is_at_goal() and not agent.is_wall_in_front():
                agent_position = agent.move()  # move right / east
            agent.turn_left()
            assert agent._Agent__get_direction() == Direction.NORTH

        # (3) move up
        while not agent.is_at_goal() and not agent.is_wall_in_front():
            agent_position = agent.move()  # move up / north

        # (4) move one step right
        agent._Agent__turn_right()
        if not agent.is_at_goal() and not agent.is_wall_in_front():
            assert agent._Agent__get_direction() == Direction.EAST
            agent_position = agent.move()  # move right
        agent._Agent__turn_right()

    goal_position = [world.get_goal_position()[0],
                     world.get_goal_position()[1]]
    assert agent_position == goal_position, f'{agent_position} != {goal_position}'


if __name__ == "__main__":
    threeRightAndUp()
    randomWalk()
    deterministicWalk()
