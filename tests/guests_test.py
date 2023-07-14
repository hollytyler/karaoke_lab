import unittest
from src.guests import Guest

class TestGuests(unittest.TestCase):

    def setUp(self):
        self.guest = [self.guest1, self.guest2]
        self.guest1 = Guest("Holly")
        self.guest2 = Guest("Rod")
