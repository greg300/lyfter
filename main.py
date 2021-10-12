from abc import ABC
import sys

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