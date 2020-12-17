import sys
import os
import time

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
    start = time.time()
    durations = []
    while current_turn < 30000000:
        # Do measurements:
        if current_turn % 10000 == 0:
            duration = time.time() - start
            durations.append(duration)
            calculate_remaining_time(durations, current_turn, 30000000, 10000)
            start = time.time()

        last_number = numbers_spoken[-1]
        for i, num in enumerate(reversed(numbers_spoken[:-1])):
            if num == last_number:
                # print(i + 1, end=", ")
                numbers_spoken.append(i + 1)
                break
        numbers_spoken.append(0)
        current_turn += 1

    return numbers_spoken[-1]


def calculate_remaining_time(durations, turn_number, total_turns, interval):
    if len(durations) < 2:
        return
    increases = tuple(
        durations[i] - durations[i - 1] for i in range(len(durations)) if i > 0
    )
    average_increase = sum(increases) / len(increases)
    remaining_periods = (total_turns - turn_number) / interval
    latest_duration = durations[-1]
    forecasted_durations = tuple(
        latest_duration + average_increase * turn
        for turn in range(int(remaining_periods))
    )
    total_remaining = sum(forecasted_durations)
    print(f"Current duration: {sum(durations)/60} minutes")
    print(f"Est. remaining time: {total_remaining/60} minutes")
    return total_remaining


if __name__ == "__main__":
    test_string = "0,3,6"
    res = main(input_string)
    print()
    print(f"The 30000000th number spoken is {res}")
