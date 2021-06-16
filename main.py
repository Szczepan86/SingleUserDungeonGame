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
        for text, direction in DIRECTIONS.items():
            if self.check_exit(position, direction):
                exits.append(text)
        return " ".join(exits)


class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self, direction_name, world):
        if world.check_exit(self.position, DIRECTIONS['direction_name']):
            self.position += DIRECTIONS['direction_name']
            print(f'You went {direction_name}')
        else:
            print(f'You can\'t go {direction_name}!')


DIRECTIONS = {
    'north': (0, 1),
    'south': (0, -1),
    'east': (1, 0),
    'west': (-1, 0)
}


def execute(player, command):
    command = command.strip()

    if DIRECTIONS(command):
        player.move(command)
        return

    print('I don\'t understand what you meant!')


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
