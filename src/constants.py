MIN_X = 4600
MAX_X = 5000
MIN_Y = 8100
MAX_Y = 8500

NUM_RIDERS = 100  # Number of Riders within the area at any instant.
MIN_DRIVERS = 100  # Minimum number of Drivers with which to run a simulation.
MAX_DRIVERS = 1000  # Maximum number of Drivers with which to run a simulation.
STEP_DRIVERS = 100  # Step size for iterating over number of Drivers across simulations.
NUM_ITERATIONS = 5  # Number of iterations for which to test each number of Drivers.

AVG_VELOCITY = 1500  # in units of 10 m/hour

DISTRIBUTION_MODE = 'normal'  # Change to 'uniform' for a uniform distribution of Riders and Drivers.

# Normal Distribution values (warning: changing these may result in Riders and Drivers generating out of bounds).
sigma_R = 30  # Rider std deviation = 300m
sigma_D = 20  # Driver std deviation = 200m
