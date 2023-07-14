import unittest
from src.room import Room
from src.songs import Song
from src.guests import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guests_in_room = []
        self.guest1 = Guest("Holly")
        self.guest2 = Guest("Rod")
        self.room_num1 = Room("1")
        self.room_num2 = Room("2")
        self.room_num3 = Room("3")

    def test_check_in_guests(self):
        self.room_num1.check_in_guest(self.guest1)
        self.assertEqual(1, len(self.guests_in_room))