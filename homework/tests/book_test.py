import unittest
from models.book import Book
from models.all_books import *

class TestBook(unittest.TestCase):
    def setUp(self):
        self.test_book1 = book1
        self.test_book2 = book2
        self.test_book3 = book3


    def testTitle(self):
        self.assertEqual("Uzumaki", self.test_book1.title)

    def testAuthor(self):
        self.assertEqual("Juno Dawson", self.test_book3.author)

    def testGenre(self):
        self.assertEqual("cyberpunk", self.test_book2.genre)

    def test_find_title(self):
        self.assertEqual(book2, find_by_title("Neuromancer"))
    


