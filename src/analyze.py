#!/usr/bin/envpython3

import math
import os
import sys

import pandas as pd
import matplotlib.pyplot as plt


class Analyzer():
    @staticmethod
    def fromCSV(csvfile):
        return Analyzer(pd.read_csv(csvfile))


    def __init__(self,dataframe):
        self._df = dataframe

        self._df['maxmins']=self._df.maxseconds/60.0


    @property
    def dataframe(self):
        return self._df


    def to_scatterplot(self):
        fig = plt.figure()

        ax = fig.add_subplot()

        self._df.plot('drivers', 'maxmins', kind='scatter', ax=ax)

        ax.set_title('Maximum Wait Time vs. Number of Drivers')

        drivers=sorted(self._df.drivers.unique())

        ax.set_xticks(drivers)

        ax.set_ylim(0,float(math.ceil(self._df.maxmins.max())))

        ax.set_ylabel('maximum wait time (mins)')
   
        fig.savefig('../drivers_vs_time.png')


if __name__=='__main__':
    usage="""Usage: analyze.py CSVFILE"""

    if not len(sys.argv)==2:
        print(usage, file=sys.stderr)
        exit(1)

    csvfile=sys.argv[1]

    if not os.path.exists(csvfile):
        print(f'Could not find "{csvfile}". Quitting.', file=sys.stderr)
        exit(2)

    a = Analyzer.fromCSV(csvfile)
       
    print(a.dataframe.head())

    a.to_scatterplot()
