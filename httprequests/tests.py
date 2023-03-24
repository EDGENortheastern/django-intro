import unittest
from httprequests.views import do_things

class TestMyStuff(unittest.TestCase):

    def test_the_obvious(self):
        self.assertEqual(True, True)

class TestMyStuff2(unittest.TestCase):

    def test_maths(self):
        self.assertEqual(do_things(), "Do")

if __name__ == '__main__':
    unittest.main()
