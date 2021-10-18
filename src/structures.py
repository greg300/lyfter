from abc import ABC

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