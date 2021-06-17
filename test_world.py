import unittest
from globals import *

# class to test
from world import World
from room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.world = World(10)

    def test_general(self):
        print('TestWorld: general')
        self.assertIsNotNone(self.world)
        self.assertIsInstance(self.world, World)

    def test_str(self):
        print('TestWorld: str')
        self.assertEqual(str(self.world), 'It\'s a 10x10 world with 0 room(s).')

    def test_add_get_room(self):
        print('TestWorld: add get room')
        self.world.add_room(Room('room_name1', 'room_description1'), (5, 5))
        self.assertEqual(str(self.world), 'It\'s a 10x10 world with 1 room(s).')
        self.assertEqual(self.world.get_room((5, 5)).name, 'room_name1')
        self.world.add_room(Room('room_name2', 'room_description2'), (5, 6))
        self.assertEqual(str(self.world), 'It\'s a 10x10 world with 2 room(s).')
        self.assertEqual(self.world.get_room((5, 6)).name, 'room_name2')
        self.world.add_room(Room('room_name3', 'room_description3'), (5, 5))
        self.assertEqual(str(self.world), 'It\'s a 10x10 world with 2 room(s).')
        self.assertEqual(self.world.get_room((5, 5)).name, 'room_name3')

    def test_check_get_exit(self):
        print('TestWorld: check get exit')
        position = (5, 5)
        self.assertFalse(self.world.check_exit(position, DIRECTIONS['north']))
        self.assertFalse(self.world.check_exit(position, DIRECTIONS['south']))
        self.assertFalse(self.world.check_exit(position, DIRECTIONS['east']))
        self.assertFalse(self.world.check_exit(position, DIRECTIONS['west']))
        self.assertEqual(self.world.get_room_exits(position), 'Exits: ')
        self.world.add_room(Room('room_north', 'room_description'), (5, 4))
        self.assertTrue(self.world.check_exit(position, DIRECTIONS['north']))
        self.assertFalse(self.world.check_exit(position, DIRECTIONS['south']))
        self.assertFalse(self.world.check_exit(position, DIRECTIONS['east']))
        self.assertFalse(self.world.check_exit(position, DIRECTIONS['west']))
        self.assertEqual(self.world.get_room_exits(position), 'Exits: north')
        self.world.add_room(Room('room_south', 'room_description'), (5, 6))
        self.assertTrue(self.world.check_exit(position, DIRECTIONS['south']))
        self.assertEqual(self.world.get_room_exits(position), 'Exits: north, south')
        self.world.add_room(Room('room_east', 'room_description'), (6, 5))
        self.assertTrue(self.world.check_exit(position, DIRECTIONS['east']))
        self.assertEqual(self.world.get_room_exits(position), 'Exits: north, south, east')
        self.world.add_room(Room('room_west', 'room_description'), (4, 5))
        self.assertTrue(self.world.check_exit(position, DIRECTIONS['west']))
        self.assertEqual(self.world.get_room_exits(position), 'Exits: north, south, east, west')

"""
    def test_attribute_update(self):
        print('TestRoom: attribute update')
        self.room.name = 'new_name'
        self.assertEqual(str(self.room), 'new_name\ntest_description')
        self.room.description = 'new_description'
        self.assertEqual(str(self.room), 'new_name\nnew_description')
        self.room.name = ['unexpected', 'list']
        self.assertEqual(str(self.room), 'default_name\nnew_description')
        self.room.description = ['unexpected', 'list']
        self.assertEqual(str(self.room), 'default_name\ndefault_description')
"""