from abc import ABC
from typing import List
from numpy import random

import sys

MIN_X = 4600
MAX_X = 5000
MIN_Y = 8100
MAX_Y = 8500

class User(ABC):
    """Abstract class representing either a Driver or a Rider."""
    pass

class Driver(User):
    """Class representing a Driver
    (Lyfter personnel providing vehicle transportation)."""
    def __init__(self, x: float, y: float) -> None:
        self.x = x  # Current latitude coorindate
        self.y = y  # Current longitude coorindate
        self.is_paired = False  # Whether the Driver is paired with a Rider

class Rider(User):
    """Class representing a Rider
    (a customer wishing to use Lyfter for transportation from start point to destination)."""
    def __init__(self, x: float, y: float) -> None:
        self.x = x  # Current latitude coorindate
        self.y = y  # Current longitude coorindate
        self.is_paired = False  # Whether the Rider is paired with a Driver

class Simulation:
    """Class to hold all details of the simulation."""
    def generate_drivers(self,
                         num_drivers: int,
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


    def generate_riders(self,
                         num_riders: int,
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

    def start(self, num_drivers: int):
        pass


if len(sys.argv) != 2:
    raise Exception(f"Invalid arguments: 1 expected, got {len(sys.argv) - 1}.")
else:
    try:
        num_drivers = int(sys.argv[1])
    except ValueError:
        raise Exception(f"Invalid argument: expected int, got {type(sys.argv[1])}.")
    
    if num_drivers < 100:
        raise Exception(f"Invalid argument: expected num_drivers >= 100, got {num_drivers}.")
    
    s = Simulation()
    s.start(num_drivers)