import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string, preamble_length):
    input_items = tuple(int(n) for n in input_string.splitlines())

    for i, number in enumerate(input_items[preamble_length:]):
        if not check_if_valid(input_items[i : i + preamble_length], number):
            return number

    print("We didn't find it.")


def check_if_valid(preamble, number):
    for i, val_a in enumerate(preamble):
        for val_b in preamble[i + 1 :]:
            if val_a + val_b == number:
                return True
    return False


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
    # res = main(test_input, 5)
    res = main(input_string, 25)
    print(f"The result is {res}")