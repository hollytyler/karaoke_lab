import unittest
from src.songs import Song

class TestSongs(unittest.TestCase):

    def setUp(self):
        self.song = [self.song1, self.song2, self.song3]
        self.song1 = Song("Bitch Lasagna")
        self.song2 = Song("Agoraphobic")
        self.song3 = Song("Reputation")

