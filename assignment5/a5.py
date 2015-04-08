#!/usr/interval:bin/python
# -*- coding: utf-8 -*-

class interval: 
    'all operations for intervals'
    def __init__(self, s):
        try: 
            if ((type(s) is str) and (s[0] == '[' or s[0] == '(') and 
                    (s[len(s)-1] == ']' or s[len(s)-1] == ')') and 
                    (len(s[1:-1].split(',')) == 2 
                    # and s[1:-1].split(',')[0].isdigit() and s[1:-1].split(',')[1].isdigit()   #uncomment if positive int only
                    ) and int(s[1:-1].split(',')[0]) - int(s[1:-1].split(',')[1]) <= 0):
                s = s.replace(" ", "")
                self.start  = int (s[1:-1].split(',')[0]) + (0 if s[0] == '[' else 1)
                self.end = int (s[1:-1].split(',')[1]) + (1 if s[len(s)-1] == ']' else 0)
                self.start_real = s[0] == '['
                self.end_real = s[len(s)-1] == ']'
            else:
                raise ValueError('incorrect data type input a string like “[1,4]", "(2,3]", "[2,3)" or "(1,4)"')
        except Exception: 
           raise 

    def intervalToArray(self):
        return range(self.start, self.end)

    def intervalToString(self):
        tmp = "[" + str(self.start) if self.start_real else "(" + str(self.start - 1)
        return tmp + "," + (str(self.end - 1) + "]" if self.end_real else str(self.end + 0) + ")")

    @staticmethod
    def intervalsOverlap(int1, int2):
        merged = sorted(int1.intervalToArray() + int2.intervalToArray())
        dedup = sorted(set(merged))
        return dedup if merged != dedup else None

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
                intervalstr += ("[" + str(dedup[0]) + ",") if int1.start_real else ("(" + str(dedup[0] - 1) + ",")
            else:
                intervalstr += ("[" + str(dedup[0]) + ",") if int2.start_real else ("(" + str(dedup[0] - 1) + ",")
            if dedup[-1] == arr1[-1]:
                intervalstr += (str(dedup[-1]) + "]") if int1.end_real else (str(dedup[-1] + 1) + ")")
            else:
                intervalstr += (str(dedup[-1]) + "]") if int2.end_real else (str(dedup[-1] + 1) + ")")
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
        return newint if intervals == "" else interval.mergeOverlapping(intervals + ',' + newint)

    @staticmethod
    def intervalAdj(int1, int2):
        a = int1.intervalToArray()
        b = int2.intervalToArray()
        tmp = range(min(a[0], b[0]), max(a[-1], b[-1]) + 1)
        return (tmp if tmp == (a + b) else None)
