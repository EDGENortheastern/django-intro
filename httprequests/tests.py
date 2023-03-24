import unittest
from httprequests.views import square_num

class SmokeTests(unittest.TestCase):

    def test_truthiness(self):
        self.assertEqual(True, True)
    
    def test_maths(self):
        self.assertEqual(2+2, 4)

class TestMyStuff2(unittest.TestCase):

    def test_function(self):
        self.assertEqual(square_num(4), 16)

if __name__ == '__main__':
    unittest.main()
