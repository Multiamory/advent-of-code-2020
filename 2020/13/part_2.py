import sys
import copy
import os
from datetime import datetime

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    bus_ids = tuple(Bus(i, num) for i, num in enumerate(input_string.split(",")))
    highest_id = max(bus_ids, key=lambda b: b.id if b.id != "x" else 0)
    # 4 is the magic number in terms of speed. Set this higher and it's slow to get started
    # set it lower and it still takes a while after getting the initial interval.
    # This could get optimized futher but I'm happy with these results for now.
    highest_buses = get_highest_buses(bus_ids, 4)

    time_to_check = highest_id.id - highest_id.index
    print("Checking departure times...")
    candidates = []
    interval = highest_id.id

    while len(candidates) < 2:
        if check_highest_buses(highest_buses, time_to_check):
            candidates.append(time_to_check)
            print("Adding candidate:", time_to_check, flush=True)
        time_to_check += interval

    interval = candidates[1] - candidates[0]
    time_to_check = candidates[0]
    while True:
        if check_subsequent_times(time_to_check, bus_ids):
            print()
            print("We did it!")
            return time_to_check
        time_to_check += interval


def check_highest_buses(highest_buses, time_to_check):
    for bus in highest_buses:
        if not bus.can_depart(time_to_check + bus.index):
            return False
    return True


def get_highest_buses(buses, num):
    my_buses = list(buses)
    highest_buses = []
    while len(highest_buses) < num:
        max_bus = max(my_buses, key=lambda b: b.id if b.id != "x" else 0)
        highest_buses.append(max_bus)
        my_buses.remove(max_bus)

    return highest_buses


def check_subsequent_times(time, buses):
    for i, bus in enumerate(buses):
        if not bus.can_depart(time + i):
            return False
    return True


class Bus:
    def __init__(self, index, bus_id):
        self.id = int(bus_id) if bus_id != "x" else bus_id
        self.index = index

    def can_depart(self, target):
        if self.id == "x":
            return True
        if target % self.id == 0:
            return True
        return False

    def __repr__(self):
        return f"Bus {self.id}"


if __name__ == "__main__":
    start = datetime.now()
    res = main(input_string.splitlines()[1])
    duration = datetime.now() - start
    print("Total Duration: ", duration.total_seconds())
    # res = main("1789,37,47,1889")
    print("result: ", res)