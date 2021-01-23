import unittest
import LibraryComplex as lcp

class testfunciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(lcp.sum_complex((4, 5), (5, 4)), (9, 9))
        self.assertEqual(lcp.sum_complex((-4, -100), (1, 4)), (-3, -96))

if __name__ == '__main__':
    unittest.main()