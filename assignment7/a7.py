import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib.backends.backend_pdf import PdfPages
from pylab import *

class trial:
    'define an investment'
    def __init__(self, num_positions, num_trials):
        self.num_positions = num_positions
        self.position_value = 1000 / num_positions 
        self.num_trials = num_trials

    @staticmethod
    def simulate(trial):
        'random lose or gain: return @cum result '
        cum_rst = [0] * trial.num_trials
        chance = np.random.uniform(0, 1, size = trial.num_trials * trial.num_positions)
        for i in range(trial.num_trials):
            day_rst = 0
            for d in range(trial.num_positions):
                if chance[i*trial.num_positions + d] <= 0.51:
                    day_rst += trial.position_value * 2
            cum_rst[i] = day_rst 
        
        return cum_rst

    @staticmethod
    def invest(positions, num_trials):
        'make investment by @positions invest combination array and @num_trials number of trials'
        f = open('results.txt','w')
        wtofile = ""
        for i in range(len(positions)):
            cumu_ret = [0] * num_trials
            cumu_ret = trial.simulate(trial(positions[i], num_trials)) 

            daily_ret = [0] * num_trials 
            for j in range(num_trials):
                daily_ret[j] = (cumu_ret[j] / 1000.0) - 1.0

            print "position ",positions[i], ", mean =", np.mean(daily_ret), ", std =", np.std(daily_ret)

            f.write("position " + str(positions[i]) + ", mean = "   + str(np.mean(daily_ret)) + ", std = " + str(np.std(daily_ret)) + "\r\n")
            f.flush()

            print "Loading figure " + str(i) + "..."
            fig = plt.figure()
            plt.hist(daily_ret, 100, range=[-1,1])
            fig.savefig('histogram_'+str(positions[i]).zfill(4)+'_pos.pdf')
            print "Figure " + str(i) + " saved. \n"

        print "Results saved in results.txt"
        plt.show(block=False)
        print "Figures would disappear in 3 seconds"
        time.sleep(3)
        plt.close('all')
        f.close()
        
if __name__ == "__main__": 
    positions = [1, 10, 100, 1000]
    num_trials = 10000

    trial.invest(positions, num_trials)
