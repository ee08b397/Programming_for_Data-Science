from a8 import *
import sys

if __name__ == '__main__':
    try:
        dataset = DataSet()
    except Exception:
        print 'dataset error'

    while(True):
        try:
            n = raw_input("Enter the year (1800 - 2012), or 'Finish'? ")
            if n == 'Finish':
                print '2007 - 2012'
                for y in range(2007, 2013, 1):
                    tools = DataAnalysisTools(str(y), dataset)
                    tools.box_plot()
                    tools.histogram_plot()
                print ''
                sys.exit(0)
            if n.isdigit() and int(n) >= 1800 and int(n) <= 2012:
                # year = int(n)
                year = n
                disp_incomeByCountry_year(year, dataset.income)
                tools = DataAnalysisTools(year, dataset)
                tools.box_plot() 
                tools.histogram_plot()
            else:
                print 'invalid year'

        except KeyboardInterrupt:
            print ''
            sys.exit(1)
        # except Exception: 
        #    pass
