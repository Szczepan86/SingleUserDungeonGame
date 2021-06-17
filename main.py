class Room:
    def __init__(self, name, description):
        """
        Room class constructor. You can define the name and description of the room.
        :param name: name of the room, e.g. 'Secret room'
        :param description: description of the room, e.g. 'This room is so secret you can't even get there'
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}\n' \
               f'{self.description}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            self._name = 'default_name'

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self._description = description
        else:
            self._description = 'default_description'


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


# static dictionary with direction vectors
DIRECTIONS = {
    'north': (0, -1),
    'south': (0, 1),
    'east': (1, 0),
    'west': (-1, 0)
}


def execute(command):
    """
    Function managing user input. If you want to add another command - you should manage it there.
    :param command: user command, e.g. 'south'
    :return:
    """
    command = command.strip()

    if command in DIRECTIONS:
        player.move(command, world)
        return

    print('I don\'t understand what you meant!')


if __name__ == '__main__':
    # player creation in the middle of world (10, 10)
    player = Player('Monty', (10, 10))

    # world creation - size 20x20
    world = World(20)

    # filling world with some rooms
    world.add_room(Room('Starting room', 'Such a lovely place to start your adventure!'), (10, 10))
    world.add_room(Room('North room', 'It\'s just an empty room at north. Nothing interesting there.'
                                      'Try to go north or south just by typing \'north\' or \'south\'.'), (10, 9))
    world.add_room(Room('South room', 'So you convinced me you can go south. Did you try east?'), (10, 11))
    world.add_room(Room('South-east room', 'Well, I think that\'s it, nothing more to explore.'), (11, 11))

    while True:
        # print room details on the screen
        print(world.get_room(player.position))
        print(world.get_room_exits(player.position))

        # get user input and make an action
        command = input('Where do you want to go? ')
        if command == 'quit':
            break
        execute(command)

        print()
