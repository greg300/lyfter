from typing import List, Tuple
from numpy import random
import math

from structures import Driver, Rider
import constants
MIN_X = constants.MIN_X
MAX_X = constants.MAX_X
MIN_Y = constants.MIN_Y
MAX_Y = constants.MAX_Y
NUM_RIDERS = constants.NUM_RIDERS
AVG_VELOCITY = constants.AVG_VELOCITY
SIGMA_R = constants.sigma_R
SIGMA_D = constants.sigma_D


class Simulation:
    """Class to hold all details of the simulation."""
    @staticmethod
    def generate_drivers(num_drivers: int,
                         min_x: float,
                         max_x: float,
                         min_y: float,
                         max_y: float
    ) -> List[Driver]:
        """Generate a list of Drivers uniformly distributed
        between the min and max x & y.
        :param num_drivers: The number of Drivers to be generated
        :param min_x: Minimum x-coordinate within which to generate users
        :param max_x: Maximum x-coordinate within which to generate users
        :param min_y: Minimum y-coordinate within which to generate users
        :param max_y: Maximum y-coordinate within which to generate users
        :returns: a list of Drivers generated
        """
        drivers = []
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2

        mu_d_e = (min_x + center_x) / 2  # Driver center, east
        mu_d_w = (center_x + max_x) / 2  # Driver center, west
        mu_d_s = (min_y + center_y) / 2  # Driver center, south
        mu_d_n = (center_y + max_y) / 2  # Driver center, north

        # Generate SW Driver quadrant positions.
        for _ in range(0, int(num_drivers / 4)):
            x = random.normal(mu_d_w, SIGMA_D)
            y = random.normal(mu_d_s, SIGMA_D)
            drivers.append(Driver(x, y))

        # Generate NW Driver quadrant positions.
        for _ in range(int(num_drivers / 4), int(2 * num_drivers / 4)):
            x = random.normal(mu_d_w, SIGMA_D)
            y = random.normal(mu_d_n, SIGMA_D)
            drivers.append(Driver(x, y))

        # Generate SE Driver quadrant positions.
        for _ in range(int(2 * num_drivers / 4), int(3 * num_drivers / 4)):
            x = random.normal(mu_d_e, SIGMA_D)
            y = random.normal(mu_d_s, SIGMA_D)
            drivers.append(Driver(x, y))

        # Generate NE Driver quadrant positions.
        for _ in range(int(3 * num_drivers / 4), num_drivers):
            x = random.normal(mu_d_e, SIGMA_D)
            y = random.normal(mu_d_n, SIGMA_D)
            drivers.append(Driver(x, y))

        return drivers

    @staticmethod
    def generate_riders(num_riders: int,
                        min_x: float,
                        max_x: float,
                        min_y: float,
                        max_y: float
    ) -> List[Rider]:
        """Generate a list of Riders uniformly distributed
        between the min and max x & y.
        :param num_riders: The number of Riders to be generated
        :param min_x: Minimum x-coordinate within which to generate users
        :param max_x: Maximum x-coordinate within which to generate users
        :param min_y: Minimum y-coordinate within which to generate users
        :param max_y: Maximum y-coordinate within which to generate users
        :returns: a list of Riders generated
        """
        riders = []
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2

        for _ in range(num_riders):
            x = random.normal(center_x, SIGMA_R)
            y = random.normal(center_y, SIGMA_R)
            riders.append(Rider(x, y))
        return riders

    @staticmethod
    def get_distance(p1 : Tuple[float, float], p2: Tuple[float, float]):
        """Calculate the distance between two points.
        :param p1: Point A
        :param p2: Point B
        :returns: distance between Point A and Point B"""
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    

    def start(self, num_drivers: int):
        """Start running a simulation for a given number of drivers.
        :param num_drivers: The number of Drivers to be tested"""
        # Generate Drivers and Riders.
        drivers = self.generate_drivers(num_drivers, MIN_X, MAX_X, MIN_Y, MAX_Y)
        riders = self.generate_riders(NUM_RIDERS, MIN_X, MAX_X, MIN_Y, MAX_Y)

        # Calculate distances from all Drivers to all Riders.
        distances = [[0 for i in range(NUM_RIDERS)] for j in range(num_drivers)]
        for i in range(num_drivers):
            d = drivers[i]
            for j in range(NUM_RIDERS):
                r = riders[j]
                dist = self.get_distance((d.x, d.y), (r.x, r.y))
                distances[i][j] = dist
        
        # Pair Drivers with the Rider at minimum distance to them.
        pairs = []  # Pairs Driver to distance to their Rider.
        max_distance = self.get_distance((MIN_X, MIN_Y), (MAX_X, MAX_Y)) + 1  # For marking paired Riders.
        for i in range(num_drivers):
            if i >= NUM_RIDERS:  # End once all Riders are paired.
                break
            d = drivers[i]
            min_dist = min(distances[i])
            min_dist_rider = distances[i].index(min_dist)
            pairs.append((d, min_dist))
            for j in range(num_drivers):
                distances[j][min_dist_rider] = max_distance  # Mark that this Rider has been paired.

        # Calculate wait times.
        wait_times = []
        for p in pairs:
            wait_times.append(p[1] / AVG_VELOCITY * 60 * 60)
        
        # Return the maximum wait time.
        return max(wait_times),drivers,riders

