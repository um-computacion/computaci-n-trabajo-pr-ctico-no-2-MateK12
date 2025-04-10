import unittest

class Test_is_palindrome(unittest.TestCase):
    def simple_palindrome_1(self):
        self.assertEqual(is_palindrome('neuquen'),True) 
    def simple_palindrome_2(self):
        self.assertEqual(is_palindrome('ana'),True) 
    def simple_palindrome_1(self):
        self.assertEqual(is_palindrome('otto'),True) 