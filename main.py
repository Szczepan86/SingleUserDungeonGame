class Room:
    def __init__(self, x, y, name, description):
        self.x = x
        self.y = y
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} ({self.x}, {self.y})\n' \
               f'{self.description}'


class World:
    def __init__(self, size):
        self.world = [[None for y in range(size)] for x in range(size)]

    def add_room(self, room):
        self.world[room.x][room.y] = room

    def get_room(self, x, y):
        try:
            return self.world[x][y]
        except IndexError:
            return None

    def check_exit(self, x, y, direction):
        if self.get_room(x + direction[0], y + direction[1]):
            return True
        return False

    def get_room_exits(self, x, y):
        exits = []
        if self.check_exit(x, y, NORTH):
            exits.append('north')
        if self.check_exit(x, y, SOUTH):
            exits.append('south')
        if self.check_exit(x, y, EAST):
            exits.append('east')
        if self.check_exit(x, y, WEST):
            exits.append('west')
        return " ".join(exits)


# constants
NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

if __name__ == '__main__':
    world = World(20)
    newRoom = Room(1, 2, 'Test Room', 'This is my test room and there\'s nothing to do!')
    world.add_room(newRoom)
    newRoom = Room(1, 1, 'Test Room', 'This is my test room and there\'s nothing to do!')
    world.add_room(newRoom)
    newRoom = Room(0, 2, 'Test Room', 'This is my test room and there\'s nothing to do!')
    world.add_room(newRoom)
    print(world.get_room(1, 2))
    print(world.get_room_exits(1, 2))
    print(world.get_room(6, 4))
    print(world.get_room_exits(6, 4))
    print(world.get_room(999, 999))
    print(world.get_room_exits(999, 999))
