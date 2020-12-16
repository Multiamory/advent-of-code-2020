import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    target_time = int(input_string.splitlines()[0])
    bus_ids = tuple(
        int(num) for num in input_string.splitlines()[1].split(",") if num != "x"
    )
    closest_departure_times = [
        get_closest_time(bus_id, target_time) for bus_id in bus_ids
    ]
    closest_departure_time = min(closest_departure_times, key=lambda x: x[1])

    print(f"Target Time: {target_time}")
    print(f"Closest Departure: {closest_departure_time}")
    print(f"Closest - Target = {closest_departure_time[1] - target_time}")
    print(
        f"Result: {(closest_departure_time[1]- target_time) * closest_departure_time[0]}"
    )


def get_closest_time(bus_id, target_time):
    departure_time = 0
    # print("Calculating bus ID ", bus_id)
    while True:
        # print(departure_time, end=", ")
        if departure_time >= target_time:
            # print()
            # print("Found closest: ", departure_time)
            return bus_id, departure_time
        departure_time += bus_id


if __name__ == "__main__":
    fake_input = """939
7,13,x,x,59,x,31,19"""

    main(input_string)