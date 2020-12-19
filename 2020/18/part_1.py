import sys
import os
import string

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    lines = input_string.splitlines()
    total = 0
    for line in lines:
        chars = [c for c in line if c != " "]
        result = calculate_line(chars)
        total += result
        print("Result", result)
    return total


def calculate_line(chars, index=None):
    res = None
    operator = None
    if not index:
        index = {"i": 0}
    while index["i"] < len(chars):
        try:
            char = int(chars[index["i"]])
        except ValueError:
            char = chars[index["i"]]

        if char == "(":
            index["i"] += 1
            char = calculate_line(chars, index)
        if char == ")":
            return res

        if isinstance(char, int):
            if operator:
                res = eval(f"{res}{operator}{char}")
                operator = None
            else:
                res = int(char)
        else:
            operator = char

        index["i"] += 1

    return res


if __name__ == "__main__":
    test_string = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    test_string = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2  "
    res = main(input_string)
    print(res)