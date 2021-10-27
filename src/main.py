import argparse

from simulation import Simulation
from csvutils import write_locations, write_results
import constants
NUM_RIDERS = constants.NUM_RIDERS
MIN_DRIVERS = constants.MIN_DRIVERS
MAX_DRIVERS = constants.MAX_DRIVERS
STEP_DRIVERS = constants.STEP_DRIVERS
NUM_ITERATIONS = constants.NUM_ITERATIONS

parser = argparse.ArgumentParser(description='Run a ride share simulation.')
parser.add_argument('mode', metavar='mode', type=int, nargs='?', default=1,
                    help='mode of operation (1 = results.csv output for analysis, 2 = direct answer)')

args = parser.parse_args()
mode = args.mode

s = Simulation()
results = []

if mode == 1:
    for num_drivers in range(MIN_DRIVERS, MAX_DRIVERS, STEP_DRIVERS):
        riders = None
        drivers = None
        for i in range(NUM_ITERATIONS):
            max_wait, drivers, riders = s.start(num_drivers)
            results.append([NUM_RIDERS, num_drivers, max_wait])
        #write_locations('locations_%04d_%04d.csv' % (NUM_RIDERS, num_drivers),
        #               drivers,
        #              riders)
    write_results('results.csv', results)

elif mode == 2:
    max_wait = 300
    num_drivers = NUM_RIDERS
    while max_wait >= 300:
        iteration_results = []
        for i in range(NUM_ITERATIONS):
            max_wait, _, _ = s.start(num_drivers)
            iteration_results.append(max_wait)
        max_wait = max(iteration_results)
        if max_wait >= 300:
            num_drivers += STEP_DRIVERS
    print(num_drivers)

else:
    print("Invalid mode. Please try again.")

 
