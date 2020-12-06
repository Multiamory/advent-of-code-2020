import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________

ROWS = tuple(row for row in range(128))
COLS = tuple(col for col in range(8))


def main():
    max_id = 0
    for entry in input_string.splitlines():
        seat = Seat(entry)
        if seat.id > max_id:
            max_id = seat.id

    print("highest ID: ", max_id)


class Seat:
    def __init__(self, char_sequence):
        self.row = get_row(char_sequence[:7])
        self.col = get_col(char_sequence[7:])
        self.id = self.row * 8 + self.col


def get_row(char_sequence):
    res = ROWS
    for char in char_sequence:
        res = partition(char, res)
    return res[0]


def get_col(char_sequence):
    res = COLS
    for char in char_sequence:
        res = partition(char, res)
    return res[0]


def partition(char, iterable):
    if char in ["F", "L"]:
        return iterable[: int(len(iterable) / 2)]
    elif char in ["B", "R"]:
        return iterable[int(len(iterable) / 2) :]
    else:
        raise Exception(f"{char} is not a valid character")


if __name__ == "__main__":
    main()