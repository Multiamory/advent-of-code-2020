import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    numbers_spoken = [int(n) for n in input_string.split(",")]
    for n in numbers_spoken:
        print(n, end=", ", flush=True)

    current_turn = len(numbers_spoken)
    while current_turn < 2020:
        if current_turn % 1000 == 0:
            print(current_turn)
        last_number = numbers_spoken[-1]
        numbers_spoken.append(
            get_next_number(current_turn, last_number, numbers_spoken)
        )
        current_turn += 1
    print(numbers_spoken)
    return numbers_spoken[-1]


def get_next_number(current_turn, last_number, numbers_spoken):
    for i in range(current_turn - 1):
        if numbers_spoken[-(i + 2)] == last_number:
            return i + 1
    return 0


if __name__ == "__main__":
    test_string = "0,3,6"
    res = main(test_string)
    print()
    print(f"The 2020th number spoken is {res}")
