import unittest
from src.is_palindrome import is_palindrome
class Test_is_palindrome(unittest.TestCase):
    def test_simple_palindrome_1(self):
        self.assertEqual(is_palindrome('neuquen'),True) 
    def test_simple_palindrome_2(self):
        self.assertEqual(is_palindrome('ana'),True) 
    def test_simple_palindrome_3(self):
        self.assertEqual(is_palindrome('otto'),True) 
    def test_polindrome_phrase_1(self):
        self.assertEqual(is_palindrome('Anita lava la tina'),True)
    def test_polindrom_phrase_2(self):
        self.assertEqual(is_palindrome('Yo hago yoga hoy'),False)
    def test_polindrom_phrase_3(self):
        self.assertEqual(is_palindrome('Aman a Panama'),True)
    def test_no_palindrome_1(self):
        self.assertEqual(is_palindrome('Hola mundo como anda'),False)
    def test_no_palindrome_2(self):
        self.assertEqual(is_palindrome('botella'),False)
    def test_no_palindrome_3(self):
        self.assertEqual(is_palindrome('rusia'),False)
    def test_edge_case_1(self):
        self.assertEqual(is_palindrome('a'),False)
    def test_edge_case_2(self):
        self.assertEqual(is_palindrome(''),False)
    def test_edge_case_3(self):
        self.assertEqual(is_palindrome('H'),False)

if __name__=="__main__":
    unittest.main()