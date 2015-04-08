'''
@author: songxiao
@date:   April 2, 2015
@desc:   simulate basic gambling
'''
from a7 import *

if __name__ == "__main__": 
    while True: 
        try:
            tmp_positions = raw_input("a list of the number of shares to buy in parallel: e.g. [1, 10, 100, 1000] ? \n")
            
            if tmp_positions == "quit":
                print 'user quit'
                break;
            if False in [s.isdigit() for s in tmp_positions.replace(" ", "")[1:-1].split(',')] or tmp_positions[0] != "["  or tmp_positions[-1] != "]":
                raise ValueError


            num_trials = raw_input("number of trials ? \n")

            if num_trials == "quit":
                print 'user quit'
                break;
            if not num_trials.isdigit() or int (num_trials) < 1:
                raise ValueError

            positions = map(int, tmp_positions[1:-1].split(','))
            num_trials = int (num_trials)
            trial.invest(positions, num_trials)
            break
            
        except ValueError:
            print 'incorrect input\n'

        except KeyboardInterrupt:
            print "user exit voluntarily"
            sys.exit(1)

        except:
            print 'invalid input\n'


'''
    positions = [1, 10, 100, 1000]
    num_trials = 10000

    trial.invest(positions, num_trials)
'''
