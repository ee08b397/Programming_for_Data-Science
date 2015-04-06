'''
@author: songxiao
@date:   April 2, 2015
@desc:   simulate basic gambling
'''
from a7 import *

if __name__ == "__main__": 
    positions = [1, 10, 100, 1000]
    num_trials = 10000

    trial.invest(positions, num_trials)
