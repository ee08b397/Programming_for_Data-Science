import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# q 1
class DataSet:
    def __init__(self):
        self.countries = pd.read_csv('countries.csv')
        self.income = pd.read_csv('indicatorgapmindergdp_per_capita_ppp.csv').T
        print self.income.head()

# q 4
def disp_incomeByCountry_year(year, income):
    print 'plot income by country against year ' + year
    plt.hist(income.ix[year].dropna().values,bins=20)
    plt.title("Distribution of income per person across all countries in "+year+"")
    plt.xlabel("income per person")
    plt.ylabel("count")
    plt.savefig('IncomeDistribution_'+year+'.pdf')
    plt.clf()

# q 5
def merge_by_year(year, dataset):
    data = pd.merge(dataset.countries, pd.DataFrame({
                    "Country":dataset.income.T['gdp pc test'],
                    "Income":dataset.income.T[year]
                }), 
            on='Country', how='inner')
    return data

# q 6
class DataAnalysisTools:
    def __init__(self, year, dataset):
        self.year = year
        self.dataset = merge_by_year(year, dataset) 

    def box_plot(self):
        print 'plot box ' + self.year
        self.dataset.boxplot('Income', by = 'Region', rot = 90)
        plt.xlabel('region')
        plt.ylabel('income per person')
        plt.savefig('box_'+self.year+'.pdf')
        plt.clf()

    def histogram_plot(self):
        print 'plot histogram ' + self.year
        plt.hist(self.dataset.T.ix['Income'].dropna().values,bins=20)
        plt.xlabel("Income per person")
        plt.ylabel("count")
        plt.savefig('histogram_'+self.year+'.pdf')
        plt.clf()

