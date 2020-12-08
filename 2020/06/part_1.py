import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main():
    input_list = split_inputs(input_string)

    total_count = 0
    for line in input_list:
        group = set(line)
        total_count += len(group)

    print("Total for all groups: ", total_count)


def split_inputs(input_string):
    lines = input_string.splitlines()
    input_list = []
    current_item = ""
    for line in lines:
        if line:
            current_item += "{}".format(line)
        else:
            input_list.append(current_item.strip())
            current_item = ""
    if current_item not in input_list:
        input_list.append(current_item.strip())
    return input_list


if __name__ == "__main__":
    main()