import unittest

# class to test
from main import World
from main import Room
from main import Player


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room('test_name', 'test_description')

    def test_general(self):
        print('TestRoom: general')
        self.assertIsNotNone(self.room)
        self.assertIsInstance(self.room, Room)
        self.assertEqual(self.room.name, 'test_name')
        self.assertEqual(self.room.description, 'test_description')

    def test_str(self):
        print('TestRoom: str')
        self.assertEqual(str(self.room), 'test_name\ntest_description')

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


