import globals as con

from player import Player
from world import World
from room import Room


player = None
world = None


def execute(command):
    """
    Function managing user input. If you want to add another command - you should manage it there.
    :param command: user command, e.g. 'south'
    :return:
    """
    command = command.strip()

    if command in con.DIRECTIONS:
        player.move(command, world)
        return

    print('I don\'t understand what you meant!')


def init():
    global player, world
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


def game():
    init()
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


if __name__ == '__main__':
    game()
