#!/usr/interval:bin/python
# -*- coding: utf-8 -*-
import sys
import time
import unittest
import numpy
from a6 import hw6 

class utest(unittest.TestCase):
    def setUp(self):
        print '---------------', time.strftime("%c"), '---------------'
        pass
        
    def test_q1(self):
        # print "\ntest\n", hw6.q1()[2]
        self.assertTrue((hw6.q1()[0] == numpy.array([[1, 6,11], [2, 7,12], [3, 8,13], [4, 9,14], [5, 10, 15]])).all(), "q1 wrong")
                
        # self.assertTrue((hw6.q1()[1] == numpy.array([[ 2,  7, 12],[ 4,  9, 14]]])).all(), "q1a wrong")
        '''
        a = (numpy.array([[ 1,  6, 11],
                [ 2,  7, 12],
                [ 3,  8, 13],
                [ 4,  9, 14],
                [ 5, 10, 15]]), numpy.array([[ 2,  7, 12],
                [ 4,  9, 14]]), numpy.array([ 6,  7,  8,  9, 10]), numpy.array([[ 2,  7, 12],
                [ 3,  8, 13],
                [ 4,  9, 14]]), numpy.array([ 6,  7,  8,  4,  9,  5, 10]))
        self.assertTrue((hw6.q1() == a).all(), "q1 wrong")
        '''


if __name__ == "__main__":
    f = open('log', 'a')
    sys.stdout = f
    unittest.main()
