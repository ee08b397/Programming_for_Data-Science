#!/usr/interval:bin/python
# -*- coding: utf-8 -*-
import sys
from a5 import interval

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
            sys.exit(1)
        except Exception: 
            print 'incorrect list of intervals'
            pass 

    while True:
        try:
            n = raw_input("Interval? ")
            if n == "quit":
                print ''
                break
            else:
                interval(n)
                list_int = interval.insert(list_int, n)
                print list_int
        except KeyboardInterrupt:
            sys.exit(1)
        except: 
            print 'Invalid interval'

