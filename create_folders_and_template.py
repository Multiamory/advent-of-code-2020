import os

FILE_TEMPLATE = """import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


"""


def main():
    year = input("Enter year: ")
    for day in range(1, 26):
        day = str(day).zfill(2)
        path = os.path.join(f"{year}", day)

        print(f"Creating template for {year}, day {day}")

        if not os.path.exists(path):
            os.makedirs(path)

        with open(os.path.join(path, "part_1.py"), "w") as f:
            f.write(FILE_TEMPLATE)

        with open(os.path.join(path, "part_2.py"), "w") as f:
            f.write(FILE_TEMPLATE)


if __name__ == "__main__":
    main()