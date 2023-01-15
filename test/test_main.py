import unittest
from src.main import Main

class Test(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(Main.is_prime(3))

if __name__ == '__main__':
    unittest.main()
