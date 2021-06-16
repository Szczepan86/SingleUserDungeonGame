class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}\n' \
               f'{self.description}'


class World:
    def __init__(self, size):
        self.world = [[None for y in range(size)] for x in range(size)]

    def add_room(self, room, position):
        self.world[position[0]][position[1]] = room

    def get_room(self, position):
        try:
            return self.world[position[0]][position[1]]
        except IndexError:
            return None

    def check_exit(self, position, direction):
        if self.get_room((position[0] + direction[0], position[1] + direction[1])):
            return True
        return False

    def get_room_exits(self, position):
        exits = []
        if self.check_exit(position, NORTH):
            exits.append('north')
        if self.check_exit(position, SOUTH):
            exits.append('south')
        if self.check_exit(position, EAST):
            exits.append('east')
        if self.check_exit(position, WEST):
            exits.append('west')
        return " ".join(exits)


# constants
NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

if __name__ == '__main__':
    world = World(20)
    world.add_room(Room('Test Room1', 'This is my test room and there\'s nothing to do!'), (1, 2))
    world.add_room(Room('Test Room2', 'This is my test room and there\'s nothing to do!'), (1, 1))
    world.add_room(Room('Test Room3', 'This is my test room and there\'s nothing to do!'), (0, 2))
    print(world.get_room((1, 2)))
    print(world.get_room_exits((1, 2)))
    print(world.get_room((6, 4)))
    print(world.get_room_exits((6, 4)))
    print(world.get_room((999, 999)))
    print(world.get_room_exits((999, 999)))
