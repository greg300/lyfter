import unittest

from simulation import Simulation
import constants
MIN_X = constants.MIN_X
MAX_X = constants.MAX_X
MIN_Y = constants.MIN_Y
MAX_Y = constants.MAX_Y
NUM_RIDERS = constants.NUM_RIDERS

class TestSimulation(unittest.TestCase):
    def test_generate_drivers(self):
        num_drivers = 100
        drivers = Simulation.generate_drivers(num_drivers, MIN_X, MAX_X, MIN_Y, MAX_Y)

        self.assertTrue(drivers is not None)
        self.assertEqual(len(drivers), num_drivers)
        for i in range(num_drivers):
            self.assertTrue(drivers[i].x <= MAX_X and drivers[i].x >= MIN_X)
            self.assertTrue(drivers[i].y <= MAX_Y and drivers[i].y >= MIN_Y)

    def test_generate_riders(self):
        num_riders = 100
        riders = Simulation.generate_drivers(num_riders, MIN_X, MAX_X, MIN_Y, MAX_Y)

        self.assertTrue(riders is not None)
        self.assertEqual(len(riders), num_riders)
        for i in range(num_riders):
            self.assertTrue(riders[i].x <= MAX_X and riders[i].x >= MIN_X)
            self.assertTrue(riders[i].y <= MAX_Y and riders[i].y >= MIN_Y)

if __name__ == '__main__':
    unittest.main()