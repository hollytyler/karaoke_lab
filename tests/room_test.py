import unittest
from src.room import Rooms
from src.songs import Songs
from src.guests import Guests

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guests_in_room = []
        self.guest1 = Guests("Holly")
        self.guest2 = Guests("Rod")
        self.room_num1 = Rooms("1")
        self.room_num2 = Rooms("2")
        self.room_num3 = Rooms("3")

    def test_check_in_guests(self):
        self.room_num1.add_guest_to_room(self.guest1)
        self.assertEqual(1, len(self.guests_in_room))