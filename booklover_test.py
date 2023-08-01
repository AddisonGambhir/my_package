#this is booklover_test.py
#import pandas as pd
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        book_lover = BookLover("Addison Gambhir", "ajg7pk@virginia.edu", "Nonfiction")
        book_lover.add_book("1984", 4)
        self.assertTrue("1984" in book_lover.book_list['book_name'].tolist())

    def test_2_add_book(self):
        book_lover = BookLover("Addison Gambhir", "ajg7pk@virginia.edu", "Nonfiction")
        book_lover.add_book("1984", 4)
        self.assertTrue("1984" in book_lover.book_list['book_name'].tolist())
        # add the same book twice. Test if it's in `book_list` only once.

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book_lover = BookLover("Addison Gambhir", "ajg7pk@virginia.edu", "Nonfiction")
        book_lover.add_book("1984", 4)
        self.assertTrue(book_lover.has_read("1984"))

    def test_4_has_read(self): 
        book_lover = BookLover("Addison Gambhir", "ajg7pk@virginia.edu", "Nonfiction")
        self.assertFalse(book_lover.has_read("Harry Potter"))
        # pass a book NOT in the list and use `assert False` to test the answer is `True`

    def test_5_num_books_read(self): 
        book_lover = BookLover("Addison Gambhir", "ajg7pk@virginia.edu", "Nonfiction")
        book_lover.add_book("Animal Farm", 4)
        book_lover.add_book("Brave New World", 5)
        book_lover.add_book("Manufacturing Consent: The Political Economy of Mass Media", 5)
        self.assertEqual(book_lover.num_books_read(), 3)
        # add some books to the list, and test num_books matches expected.

    def test_6_fav_books(self):
        book_lover = BookLover("Addison Gambhir", "ajg7pk@virginia.edu", "Nonfiction")
        book_lover.add_book("1984", 4)
        book_lover.add_book("Animal Farm", 3)
        book_lover.add_book("Brave New World", 5)
        book_lover.add_book("Manufacturing Consent: The Political Economy of Mass Media", 5)
        fav_books_df = book_lover.fav_books()
        self.assertTrue((fav_books_df['book_rating'] > 3).all())
        # add some books with ratings to the list, making sure some of them have rating > 3.
        # Your test should check that the returned books have rating  > 3

if __name__ == '__main__':
    unittest.main(verbosity=3)
