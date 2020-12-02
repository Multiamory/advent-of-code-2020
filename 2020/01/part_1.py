import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main():
    input_values = [int(line) for line in input_string.splitlines()]
    matching_values = find_matching_values(input_values, 2020)
    print(f"The two values are {matching_values[0]} and {matching_values[1]}")
    print(f"The product is {matching_values[0] * matching_values[1]}")


def find_matching_values(values, target):
    for i, value_a in enumerate(values):
        for value_b in values[i + 1 :]:
            if value_a + value_b == target:
                return value_a, value_b


if __name__ == "__main__":
    main()