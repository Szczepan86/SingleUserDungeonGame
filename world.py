from globals import *


class World:
    def __init__(self, size):
        """
        World class constructor. You can define size of the world there (size x size)
        :param size: just size of the world, e.g. 100
        """
        self.world = [[None for y in range(size)] for x in range(size)]

    def add_room(self, room, position):
        """
        Add new room to the world map.
        :param room: Room instance
        :param position: position of the room, e.g. (10, 11)
        :return: None
        """
        self.world[position[0]][position[1]] = room

    def get_room(self, position):
        """
        Retrieve a room instance according to its position.
        :param position: position of the room, e.g. (10, 11)
        :return: Room instance or None if nothing found
        """
        try:
            return self.world[position[0]][position[1]]
        except IndexError:
            return None

    def check_exit(self, position, direction):
        """
        Check whether there's a room at selected direction.
        :param position: position of the player, e.g. (10, 10)
        :param direction: direction vector, e.g. (0, 1)
        :return: True or False
        """
        if self.get_room((position[0] + direction[0], position[1] + direction[1])):
            return True
        return False

    def get_room_exits(self, position):
        """
        Calculate and return all exits from selected location.
        :param position: position of the player, e.g. (10, 10)
        :return: String with all exits listed, e.g. 'Exits: north, south'
        """
        exits = []
        for text, direction in DIRECTIONS.items():
            if self.check_exit(position, direction):
                exits.append(text)
        return f'Exits: {", ".join(exits)}'
