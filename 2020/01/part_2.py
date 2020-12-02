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
    print(
        f"The three values are {matching_values[0]}, {matching_values[1]} and {matching_values[2]}"
    )
    print(
        f"The product is {matching_values[0] * matching_values[1] * matching_values[2]}"
    )


def find_matching_values(values, target):
    for a, value_a in enumerate(values):
        for b, value_b in enumerate(values[a + 1 :]):
            for value_c in values[b + a + 1 :]:
                if value_a + value_b + value_c == target:
                    return value_a, value_b, value_c


if __name__ == "__main__":
    main()