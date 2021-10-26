#!/usr/bin/envpython3

import math
import os
import sys

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

matplotlib.rcParams["figure.dpi"] = 200.0


class ResultsAnalyzer():
    @staticmethod
    def fromCSV(csvfile):
        return ResultsAnalyzer(pd.read_csv(csvfile))


    def __init__(self, dataframe):
        self._df = dataframe

        self._df['maxmins']=self._df.maxseconds/60.0


    @property
    def dataframe(self):
        return self._df


    def to_scatterplot(self):
        plt.style.use('ggplot')

        fig = plt.figure(figsize=(14,8))

        ax = fig.add_subplot()

        self._df.plot('drivers', 'maxmins', kind='scatter', ax=ax)

        ax.set_title('Maximum Wait Time vs. Number of Drivers')

        drivers=sorted(self._df.drivers.unique())

        step = max(1, len(drivers) // 20)

        ax.set_xticks(drivers[::step])

        ax.set_ylim(0,float(math.ceil(self._df.maxmins.max())))

        ax.set_ylabel('maximum wait time (mins)')

        fig.savefig('drivers_vs_time.png')


class LocationsAnalyzer():
    @staticmethod
    def fromCSV(csvfile):
        return LocationsAnalyzer(pd.read_csv(csvfile))


    def __init__(self, dataframe):
        self._df = dataframe

        self._df['x_meters'] = self._df.x * 10
        self._df['y_meters'] = self._df.y * 10



    @property
    def dataframe(self):
        return self._df


    def to_scatterplot(self):
        plt.style.use('ggplot')

        orange = matplotlib.colors.hex2color('#3465a4')
        blue = matplotlib.colors.hex2color('#ff8000')
        colormap = { 'rider':orange, 'driver':blue }

        self._df['color'] = \
            self._df.type.apply(lambda x: colormap[x])

        fig = plt.figure(figsize=(12,12))

        ax = fig.add_subplot()

        self._df.plot('x_meters', 'y_meters', kind='scatter', ax=ax, c=self._df.color)

        ax.set_title('Rider and Driver Locations')

        matplotlib.rcParams["legend.loc"] = 'upper right'
        ax.legend([Patch(color=blue), Patch(color=orange)],
                  ['drivers', 'riders'])


        ax.set_xlabel('x (meters)')
        ax.set_ylabel('y (meters)')

        counts = self._df.groupby(['type']).count()
        num_drivers = counts.loc['driver', 'x']
        num_riders = counts.loc['rider', 'x']
        outfile = 'locations_%04d_riders_by_%04d_drivers.png' % (num_riders, num_drivers)

        fig.savefig(outfile)


if __name__=='__main__':
    usage="""Usage: analyzer.py results|locations CSVFILE"""

    if not len(sys.argv)==3:
        print(usage, file=sys.stderr)
        exit(1)

    analysis = sys.argv[1].lower()
    csvfile = sys.argv[2]

    if not os.path.exists(csvfile):
        print(f'Could not find "{csvfile}". Quitting.', file=sys.stderr)
        exit(2)

    a = None

    if analysis == 'results':
        a = ResultsAnalyzer.fromCSV(csvfile)
    else:
        a = LocationsAnalyzer.fromCSV(csvfile)

    print(a.dataframe.head())

    a.to_scatterplot()
