from globals import *


class Player:
    def __init__(self, name, position):
        """
        Constructor class, just define name and starting position of the player.
        :param name: name of the player, e.g. 'George'
        :param position: starting position, e.g. (10, 10)
        """
        self.name = name
        self.position = position

    def move(self, direction_name, world):
        """
        Move your player to another room (if possible).
        :param direction_name: direction where you want to go, e.g. 'south'
        :param world: World instance
        :return: None
        """
        if world.check_exit(self.position, DIRECTIONS[direction_name]):
            self.position = (self.position[0] + DIRECTIONS[direction_name][0],
                             self.position[1] + DIRECTIONS[direction_name][1])
            print(f'You went {direction_name}')
        else:
            print(f'You can\'t go {direction_name}!')
