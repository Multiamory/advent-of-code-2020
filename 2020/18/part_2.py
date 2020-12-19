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
        line = "".join([c for c in line if c != " "])
        result = do_line(line)
        total += result
        print("Result", result)
    return total


def do_line(line):
    openings = []
    pairs = []
    for i, c in enumerate(line):
        if c == "(":
            openings.append(i)
        elif c == ")":
            match = openings.pop()
            if len(openings) == 0:
                pairs.append((match, i))
    for pair in reversed(pairs):
        line = line.replace(
            line[pair[0] : pair[1] + 1],
            str(do_line(line[pair[0] + 1 : pair[1]])),
        )

    return calculate_section(line)


def do_addition(section):
    res = 0
    numbers = section.split("+")
    for number in numbers:
        res += int(number)
    return res


def calculate_section(line):
    sections = line.split("*")
    product = 1
    for section in sections:
        product *= do_addition(section)

    return product


if __name__ == "__main__":
    # test_string = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    # test_string = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    # test_string = "2 * 3 + (4 * 5)"
    res = main(input_string)
    print(res)