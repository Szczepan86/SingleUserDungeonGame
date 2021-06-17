from globals import *


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
