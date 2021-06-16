class Room():
    def __init__(self, x, y, name, description):
        self.x = x
        self.y = y
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name} ({self.x}, {self.y})\n' \
               f'{self.description}'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    room = Room(1, 2, 'Test Room', 'This is my test room and there\'s nothing to do!')
    print(room)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
