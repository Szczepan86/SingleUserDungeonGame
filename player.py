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

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if isinstance(position, tuple) and all(isinstance(n, int) for n in position) and len(position) == 2:
            self._position = position
        else:
            self._position = (0, 0)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            self._name = 'default_name'