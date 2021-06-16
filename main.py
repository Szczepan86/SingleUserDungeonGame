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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    world = World(20)
    newRoom = Room(1, 2, 'Test Room', 'This is my test room and there\'s nothing to do!')
    world.add_room(newRoom)
    print(world.get_room(1, 2))
    print(world.get_room(6, 4))
    print(world.get_room(999, 999))
