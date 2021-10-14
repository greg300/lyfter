import sys

from simulation import Simulation

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