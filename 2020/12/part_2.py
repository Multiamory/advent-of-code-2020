import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________

import day12

if __name__ == "__main__":
    input_lines = input_string.splitlines()
    #     input_lines = """F10
    # N3
    # F7
    # R90
    # F11""".splitlines()

    pos = (0, 0)
    waypoint = (10, 1)

    for line in input_lines:
        pos, waypoint = day12.waypoint_operation(pos, waypoint, line)
        print(line, pos, waypoint)

    print(pos)
    print(abs(pos[0]) + abs(pos[1]))