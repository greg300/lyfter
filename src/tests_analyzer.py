import unittest

from analyzer import ResultsAnalyzer
import constants

class TestAnalyzer(unittest.TestCase):

    def test_fromCSV(self):
        csv_data = ResultsAnalyzer.fromCSV('test_data.csv')
        over_count = 0 
        for i in range(len(csv_data.dataframe)):
            if csv_data.dataframe['maxmins'][i] > 5:
                over_count += 1
        print(f'Given Test Data:')
        print(f'Out of {len(csv_data.dataframe)} wait times, there are {over_count} times when the wait time exceeds 5 minutes.')
        csv_data.to_scatterplot()
        self.assertEqual(over_count, 0)

    def test_simul(self):
        csv_data = ResultsAnalyzer.fromCSV('results.csv')
        over_count = 0 
        for i in range(len(csv_data.dataframe)): 
            if csv_data.dataframe['maxmins'][i] > 5: 
                over_count += 1 
        print(f'Simulated Data:')
        print(f'Out of {len(csv_data.dataframe)} wait times, there are {over_count} times when the wait time exceeds 5 minutes.')
        csv_data.to_scatterplot()
        self.assertEqual(over_count, 0)

    def test_drivers(self): 
        csv_data = ResultsAnalyzer.fromCSV('results.csv')
        max_drivers = csv_data.dataframe['drivers'].max()
        min_drivers = csv_data.dataframe['drivers'].min() 
        print(f'The maximum number of drivers is {max_drivers} and the minimum number of drivers is {min_drivers}')
        for i in range(len(csv_data.dataframe['drivers'])):
            self.assertTrue(csv_data.dataframe['drivers'][i] <= max_drivers)
            self.assertTrue(csv_data.dataframe['drivers'][i] >= min_drivers)
        self.assertEqual(max_drivers, 4900)
        self.assertEqual(min_drivers, 1000)

    def test_riders(self):
        csv_data = ResultsAnalyzer.fromCSV('results.csv')
        max_riders = csv_data.dataframe['customers'].max()
        min_riders = csv_data.dataframe['customers'].min()
        print(f'The maximum number of riders is {max_riders} and the minimum number of riders is {min_riders}') 
        self.assertEqual(min_riders, constants.NUM_RIDERS)
        self.assertEqual(min_riders, constants.NUM_RIDERS)

    def test_iterate(self):
        csv_data = ResultsAnalyzer.fromCSV('results.csv')
        iters = len(csv_data.dataframe)
        print(f'You have ran {iters} iterations to generate the riders and drivers')
        iter_bool = iters == 800
        self.assertEqual(iter_bool,True)

if __name__ == '__main__':
    unittest.main()
