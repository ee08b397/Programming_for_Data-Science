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
    
'''
e0 = interval("sjkkd")
e1 = interval("[jkkd")
e2 = interval("[jkk]")
e3 = interval("[jk,k]")
e4 = interval("[3,7,10]")
'''

'''
a = interval("[3,7]")
b = interval("(3,7]")
c = interval("[3,7)")
d = interval("(3,7)")
print "[3,7] " 
print a.intervalToArray()
print "(3,7] " 
print b.intervalToArray()
print "[3,7) "
print c.intervalToArray()
print "(3,7) "
print d.intervalToArray()
'''


'''
print "[3,7] merge [2,5]"
print interval.intervalToString(interval.mergeIntervals(interval("[3,7]"), interval("[2,5]")))

print "(3,7) merge (2,5)"
print interval.intervalToString(interval.mergeIntervals(interval("(3,7)"), interval("(2,5)")))

print "[4,9) merge (2,5)"
print interval.intervalToString(interval.mergeIntervals(interval("[4,9)"), interval("(2,5)")))

print "(3,7) merge (7,10)"
print interval.mergeIntervals(interval("(3,7)"), interval("(7,10)"))
'''

'''
print '\n[1,3)'
print interval.mergeOverlapping('[1,3)')

print '\n[1,3),[2,4),[3,6],(1,3]'
print interval.mergeOverlapping('[1,3),[2,4),[3,6],(1,3]')

ccc = '[1,3),[3,7)'
print '\n' + ccc
print interval.mergeOverlapping(ccc)

ddd = '[1,5], [2,6), (8,10], [8,18]'
print '\n' + ddd
print interval.mergeOverlapping(ddd)
'''

'''
a4 = "[1,3], [6,9]"
a41 = "[2,5]"
print '\ninsert(' + a4 + ', ' + a41 + ')'
print interval.insert(a4, a41)

a4 = "[1,2], (3,5), [6,7), (8,10], [12,16]"
a41 = "[4,9]"
print '\ninsert(' + a4 + ', ' + a41 + ')'
print interval.insert(a4, a41)
'''

'''
print interval.mergeAdj(range(1,6), range(7,10))
print interval.mergeAdj(range(1,7), range(7,10))
'''
