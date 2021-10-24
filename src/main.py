import argparse

from constants import NUM_RIDERS
from simulation import Simulation
from csvutils import write_locations, write_results

parser = argparse.ArgumentParser(description='Run a ride share simulation.')
parser.add_argument('--min_drivers', metavar='min_drivers', type=int, nargs='?', default=NUM_RIDERS,
                    help='minimum number of drivers in the simulation')
parser.add_argument('--max_drivers', metavar='max_drivers', type=int, nargs='?', default=2*NUM_RIDERS,
                    help='maximum number of drivers in the simulation')
parser.add_argument('--step_drivers', metavar='step_drivers', type=int, nargs='?', default=1,
                    help='step size in iterating from min_drivers to _max_drivers')
parser.add_argument('num_iterations', metavar='num_iterations', type=int, nargs='+',
                    help='number of iterations to run each simulation')

args = parser.parse_args()
num_iterations = args.num_iterations[0]

s = Simulation()
results = []

for num_drivers in range(args.min_drivers, args.max_drivers, args.step_drivers):
    riders = None
    drivers = None
    for i in range(num_iterations):
        max_wait,drivers,riders = s.start(num_drivers)
        results.append([NUM_RIDERS, num_drivers, max_wait])
    write_locations('locations_%04d_%04d.csv' % (NUM_RIDERS, num_drivers),
                    drivers,
                    riders)

write_results('results.csv', results)
 
