import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


import math


def main():
    input_lines = input_string.splitlines()

    fuel_total = 0
    fuel_with_fuel_total = 0
    for module in input_lines:
        fuel_total += get_fuel_from_mass(module)
        fuel_with_fuel_total += get_fuel_from_mass_recursive(module)

    print("Initial Estimate:", fuel_total)
    print("Including Fuel:  ", fuel_with_fuel_total)


def get_fuel_from_mass(mass):
    mass = int(mass)
    res = math.floor(mass / 3) - 2
    return res if res > 0 else 0


def get_fuel_from_mass_recursive(mass):
    mass = int(mass)
    total_mass = 0
    while mass > 0:
        mass = get_fuel_from_mass(mass)

        total_mass += mass
    return total_mass


if __name__ == "__main__":
    main()
