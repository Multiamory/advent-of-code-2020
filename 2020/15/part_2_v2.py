import sys
import os
import time

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________

TOTAL_TURNS = 30000000
MEASUREMENT_INTERVAL = 100000


def main(input_string):
    starting_numbers = tuple(int(n) for n in input_string.split(","))
    for num in starting_numbers:
        print(num, end=", ")
    print()
    numbers_spoken = {n: i + 1 for i, n in enumerate(starting_numbers[:-1])}
    latest_number = starting_numbers[-1]

    turn = len(starting_numbers) + 1
    start_time = time.time()
    while turn <= TOTAL_TURNS:
        if turn % MEASUREMENT_INTERVAL == 0:
            print(turn, time.time() - start_time)
        numbers_spoken, latest_number = do_turn(turn, numbers_spoken, latest_number)
        # print(latest_number, end=", ", flush=True)
        turn += 1
    print(f"Total Duration: {time.time() - start_time}")
    return latest_number


def do_turn(turn, numbers_spoken, latest_number):
    next_number = numbers_spoken.get(latest_number)
    if next_number:
        next_number = turn - 1 - next_number
    else:
        next_number = 0
    numbers_spoken[latest_number] = turn - 1
    return numbers_spoken, next_number


if __name__ == "__main__":
    test_string = "0,3,6"
    res = main(input_string)
    print()
    print(f"The 30000000th number spoken is {res}")
