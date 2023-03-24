import unittest

class TestMyStuff(unittest.TestCase):

    def test_the_obvious(self):
        self.assertEqual(True, True)

class TestMyStuff2(unittest.TestCase):

    def test_maths(self):
        self.assertEqual(2+2, 4)

if __name__ == '__main__':
    unittest.main()
