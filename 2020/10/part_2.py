import sys
import os
import math

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(series):
    multipliers = []
    seq_lengths = []
    set_length = 1
    previous = 0
    for num in series:
        if num - previous == 1:
            set_length += 1
        elif set_length == 3:
            seq_lengths.append(set_length)
            multipliers.append(2)
            set_length = 1
        elif set_length > 3:
            seq_lengths.append(set_length)
            multipliers.append((3 * pow(2, set_length - 4)) + 1)
            set_length = 1
        else:
            set_length = 1
        previous = num

    print(seq_lengths)
    print(multipliers)

    return math.prod(multipliers)


if __name__ == "__main__":
    inputs = [int(n) for n in input_string.splitlines()]
    inputs = sorted(inputs)
    res = main(inputs)

    print(f"There are {res} total possibilities")