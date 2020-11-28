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
    for module in input_lines:
        fuel_total += get_fuel_from_mass(module)

    print("Total fuel needed:", fuel_total)


def get_fuel_from_mass(mass):
    mass = int(mass)
    res = math.floor(mass / 3) - 2
    return res if res > 0 else 0


if __name__ == "__main__":
    main()
