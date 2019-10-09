import unittest
from listutil import *

class TestListUtil(unittest.TestCase):
    """
    =======
    test on unique funtion start here.
    =======
    """

    def test_unique_single(self):
        """ test function unique on single element in list"""
        # 1 element in list test
        self.assertEqual([5], unique([5]))
        self.assertEqual([101], unique([101]))
        self.assertEqual(['BOO!'], unique(['BOO!']))

    def test_unique_multiple(self):
        """ test function unique on multiple element in list"""
        # duplicate list element
        self.assertEqual(['hi'], unique(['hi', 'hi', 'hi']))
        # unordered list element
        self.assertEqual([4,100, 0], unique([4, 100, 4, 4, 4, 100, 0]))
        # dulplicate and unordered list element
        self.assertEqual(["b","a"], unique(["b","a","a","b","b","b","a","a"]))

    def test_unique_edge(self):
        """ test function unique on edge case"""
        # empty list test
        self.assertEqual([], unique([]))
        # argument not a list
        with self.assertRaises(TypeError): unique(100000)
            

    """
    =======
    test on average funtion start here.
    =======
    """

    def test_average_single(self):
        """ test function average on sigle element in list"""
        # 1 element in list test
        self.assertEqual(0.0, average([0]))
        self.assertEqual(5.0, average([5]))

    def test_average_multiple(self):
        """ test function average on multiple element in list """
        # multiple element in list test
        self.assertEqual(1.0, average([1, 1]))
        self.assertEqual(5.0, average([2, 4, 6, 8]))
        
    
    def test_average_edge(self):
        """ test function average on weird case"""
        # empty list test
        with self.assertRaises(TypeError): average(1)