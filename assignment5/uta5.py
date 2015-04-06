#!/usr/interval:bin/python
# -*- coding: utf-8 -*-
import sys
import unittest
from a5 import interval


# print interval.insert('[1,3],[6,9]', '[2,5]')

class utest(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_Merge2(self):
        self.assertEqual(interval.mergeIntervals(interval('[1,3]'), interval('[2,5]')).intervalToString(), '[1,5]')
        self.assertEqual(interval.mergeIntervals(interval('(1,13)'), interval('[2,25]')).intervalToString(), '(1,25]')
        
        # test no overlap exception
        # self.assertEqual(interval.mergeIntervals(interval('[1,3]'), interval('[5,8]')).intervalToString(), '[1,5]')

    def test_MergeOvp(self):
        self.assertEqual(interval.mergeOverlapping('[1,5],[2,6),(8,10],[8,18]'), '[1,5],[8,18]')

    def test_MergeAdj(self):
        self.assertEqual(interval.intervalAdj(interval('[1,3]'), interval('[5,7]')), None)
        self.assertEqual(interval.intervalAdj(interval('[1,3]'), interval('[4,7]')), range(1,8))

    def test_InsertInt(self):
        self.assertEqual(interval.insert('[1,3],[6,9]', '[2,5]'), '[1,9]')
        self.assertEqual(interval.insert('[1,2], (3,5), [6,7), (8,10], [12,16]', '[4,9]'), '[1,2],(3,10],[12,16]')


if __name__ == "__main__":
    unittest.main()
