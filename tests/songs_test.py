import unittest
from src.songs import Songs

class TestSongs(unittest.TestCase):

    def setUp(self):
        self.song = [self.song1, self.song2, self.song3]
        self.song1 = Songs("Bitch Lasagna")
        self.song2 = Songs("Agoraphobic")
        self.song3 = Songs("Reputation")

