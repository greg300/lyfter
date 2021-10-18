import argparse
import csv

from constants import NUM_RIDERS
from simulation import Simulation

parser = argparse.ArgumentParser(description='Run a ride share simulation.')
parser.add_argument('num_iterations', metavar='num_iterations', type=int, nargs='+',
                    help='number of iterations to run each simulation')

args = parser.parse_args()
num_iterations = args.num_iterations[0]

s = Simulation()
results = []

for num_drivers in range(100, 150):
    for i in range(num_iterations):
        max_wait = s.start(num_drivers)
        results.append([NUM_RIDERS, num_drivers, max_wait])

with open('../results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["customers", "drivers", "maxseconds"])
    writer.writerows(results)
