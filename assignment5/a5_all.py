#!/usr/interval:bin/python
# -*- coding: utf-8 -*-
import sys

class interval: 
    'all operations for intervals'
    start = 0
    end   = 0
    start_real = False 
    end_real   = False
    def __init__(self, s):
        try: 
            if (
                    (type(s) is str) and 
                    (s[0] == '[' or s[0] == '(') and 
                    (s[len(s)-1] == ']' or s[len(s)-1] == ')') and 
                    (len(s[1:-1].split(',')) == 2 
                    #   and
                    #    s[1:-1].split(',')[0].isdigit() and 
                    #    s[1:-1].split(',')[1].isdigit()
                    ) and
                    int(s[1:-1].split(',')[0]) - int(s[1:-1].split(',')[1]) <= 0
                ):
                s = s.replace(" ", "")
                if (s[0] == '['):
                    self.start  = int (s[1:-1].split(',')[0])
                    self.start_real = True
                else: 
                    self.start = int (s[1:-1].split(',')[0]) + 1
                    self.start_real = False 

                if (s[len(s)-1] == ']'):
                    self.end = int (s[1:-1].split(',')[1]) + 1
                    self.end_real = True
                else: 
                    self.end = int (s[1:-1].split(',')[1]) 
                    self.end_real = False 

            else:
                raise ValueError('incorrect data type input a string like “[1,4]", "(2,3]", "[2,3)" or "(1,4)"')
        except Exception: 
           raise 
            #print 'incorrect data type input a string like “[1,4]", "(2,3]", "[2,3)" or "(1,4)"'

    def intervalToArray(self):
        return range(self.start, self.end)

    def intervalToString(self):
        tmp = "" 
        if self.start_real:
            tmp += "[" + str(self.start)
        else:
            tmp += "(" + str(self.start - 1)
        if self.end_real:
            tmp += "," + str(self.end - 1) + "]"
        else:
            tmp += "," + str(self.end + 0) + ")"
        return tmp

    @staticmethod
    def intervalsOverlap(int1, int2):
        arr1 = int1.intervalToArray()
        arr2 = int2.intervalToArray()
        merged = sorted(arr1 + arr2)
        dedup = sorted(set(merged))
        if (merged != dedup):
            return dedup 
        else:
            return None 

    @staticmethod
    def mergeIntervals(int1, int2):
        dedup = interval.intervalsOverlap(int1, int2)
        intad = interval.intervalAdj(int1, int2)
        if dedup != None or intad != None:
            dedup = (intad if dedup == None else dedup)
            arr1 = int1.intervalToArray()
            arr2 = int2.intervalToArray()
            intervalstr = ""
            if dedup[0] == arr1[0]:
                if int1.start_real:
                    intervalstr += "[" + str(dedup[0]) + ","
                else:
                    intervalstr += "(" + str(dedup[0] - 1) + ","
            else:
                if int2.start_real:
                    intervalstr += "[" + str(dedup[0]) + ","
                else:
                    intervalstr += "(" + str(dedup[0] - 1) + ","

            if dedup[-1] == arr1[-1]:
                if int1.end_real:
                    intervalstr += str(dedup[-1]) + "]"
                else:
                    intervalstr += str(dedup[-1] + 1) + ")"
            else:
                if int2.end_real:
                    intervalstr += str(dedup[-1]) + "]"
                else:
                    intervalstr += str(dedup[-1] + 1) + ")"
            return interval(intervalstr) 
        else:
            raise Exception("No overlap")

    @staticmethod
    def mergeOverlapping(intervals):
        intervals = intervals.replace(" ", "")
        tmp_array = intervals.split(",")
        lst_intervals = []
        if len(tmp_array) == 2:
            return intervals;
        for i in range(0, len(tmp_array) - 1, 2):
            lst_intervals.append(interval(tmp_array[i] + ',' + tmp_array[i+1]))
        i = 0
        j = 1
        while(i < len(lst_intervals) - 1):
            if (interval.intervalsOverlap(lst_intervals[i], lst_intervals[j]) != None) or (interval.intervalAdj(lst_intervals[i], lst_intervals[j]) != None):
                lst_intervals[i] = interval.mergeIntervals(lst_intervals[i], lst_intervals[j])
                lst_intervals.pop(j)
                j = i + 1
            else:
                j += 1
            if j >= len(lst_intervals):
                i += 1
                j = i + 1
        out_str = ""
        for i in range(0, len(lst_intervals) - 1):
            out_str += lst_intervals[i].intervalToString() + ","
        out_str += lst_intervals[-1].intervalToString()
        return out_str
        
    @staticmethod
    def insert(intervals, newint):
        if intervals == "":
            return newint
        else:
            return interval.mergeOverlapping(intervals + ',' + newint)

    @staticmethod
    def intervalAdj(int1, int2):
        a = int1.intervalToArray()
        b = int2.intervalToArray()
        tmp = range(min(a[0], b[0]), max(a[-1], b[-1]) + 1)
        return (tmp if tmp == (a + b) else None)



















'''
if __name__ == "__main__":
    while True:
        try:
            list_int = raw_input("List of intervals? ")
            if list_int == "quit":
                print ''
                sys.exit(1)

            list_int = interval.mergeOverlapping(list_int)
            print list_int
            break
        except KeyboardInterrupt:
            print ''
            sys.exit(1)
        except Exception: 
            print 'incorrect list of intervals'
            pass 

    while True:
        try:
            n = raw_input("Interval? ")
            if n == "quit":
                print ''
                sys.exit(1)
            else:
                interval(n)
                list_int = interval.insert(list_int, n)
                print list_int
        except KeyboardInterrupt:
            print ''
            sys.exit(1)
        except: 
            print 'Invalid interval'
            #pass 
'''

'''
e0 = interval("sjkkd")
e1 = interval("[jkkd")
e2 = interval("[jkk]")
e3 = interval("[jk,k]")
e4 = interval("[3,7,10]")

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

'''
import unittest
class utest(unittest.TestCase):
    def setUp(self):
        pass

    def test_MergeAdj(self):
        self.assertEqual(interval.intervalAdj(interval('[1,3]'), interval('[5,7]')), None)
        self.assertEqual(interval.intervalAdj(interval('[1,3]'), interval('[4,7]')), range(1,8))

if __name__ == "__main__":
    #utest.utMergeAdj()
    unittest.main()

'''

