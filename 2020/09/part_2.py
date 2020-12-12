import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string, target):
    input_items = tuple(int(n) for n in input_string.splitlines())
    sequence = find_sequence_that_sums(input_items, 2, target)
    return min(sequence) + max(sequence)


def find_sequence_that_sums(input_items, num_items, target):
    print(f"Checking sequences of length {num_items}")
    if num_items == len(input_items):
        raise Exception("We didn't find it...")
    for i, starting_point in enumerate(input_items[: len(input_items) - num_items]):
        if sum(input_items[i : i + num_items]) == target:
            return input_items[i : i + num_items]
    return find_sequence_that_sums(input_items, num_items + 1, target)


if __name__ == "__main__":
    test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
    # res = main(test_input, 127)
    res = main(input_string, 1398413738)
    print(f"The result is {res}")