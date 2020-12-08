import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    input_list = split_inputs(input_string)

    total_count = 0
    for group in input_list:
        group_count = count_shared_answers(group)
        total_count += group_count

    return total_count


def count_shared_answers(group_inputs):
    common_letters = list(group_inputs[0])
    for individual in group_inputs:
        common_letters = [letter for letter in common_letters if letter in individual]

    return len(common_letters)


def split_inputs(input_string):
    lines = input_string.splitlines()
    input_list = []
    current_item = []
    for line in lines:
        if line:
            current_item.append(line)
        else:
            input_list.append(current_item)
            current_item = []

    input_list.append(current_item)
    return input_list


if __name__ == "__main__":
    total_count = main(input_string)
    print("Total for all groups: ", total_count)
