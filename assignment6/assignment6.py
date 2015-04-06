from a6 import hw6 
import sys

if __name__ == '__main__':
    try:
        hw6.q1()
        hw6.q2()
        hw6.q3()
        hw6.q4()
    except KeyboardInterrupt:
        print "user exit voluntarily"
        sys.exit(1)
