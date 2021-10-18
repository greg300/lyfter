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
        for _ in range(num_drivers):
            x = random.uniform(min_x, max_x)
            y = random.uniform(min_y, max_y)
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
        for _ in range(num_riders):
            x = random.uniform(min_x, max_x)
            y = random.uniform(min_y, max_y)
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