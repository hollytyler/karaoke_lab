import unittest
from src.guests import Guests

class TestGuests(unittest.TestCase):

    def setUp(self):
        self.guest = [self.guest1, self.guest2]
        self.guest1 = Guests("Holly")
        self.guest2 = Guests("Rod")
