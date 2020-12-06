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
    entries = input_string.splitlines()
    id_list = sorted([Seat(entry).id for entry in entries])

    previous_id = 0
    for seat_id in id_list:
        if previous_id + 2 == seat_id:
            return Seat(seat_id - 1), id_list
        previous_id = seat_id


class Seat:
    def __init__(self, char_sequence_or_id):
        if isinstance(char_sequence_or_id, str):
            self.row = get_row(char_sequence_or_id[:7])
            self.col = get_col(char_sequence_or_id[7:])
            self.id = self.row * 8 + self.col
        elif isinstance(char_sequence_or_id, int):
            self.id = char_sequence_or_id
            self.row = self.id // 8
            self.col = self.id % 8


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


RED = "\u001b[41m"
GREY = "\u001b[100m"
GREEN = "\u001b[42m"
RESET = "\u001b[0m"


def print_results(id_list, my_seat_id):
    for seat_id in range(1024):
        if seat_id == my_seat_id:
            print(f"{GREEN}{str(seat_id).center(5)}{RESET}", end=" ")
        elif seat_id not in id_list:
            print(f"{RED}{str(seat_id).center(5)}{RESET}", end=" ")
        else:
            print(f"{GREY}{str(seat_id).center(5)}{RESET}", end=" ")

        if (seat_id + 1) % 8 == 0:
            print()
        elif seat_id % 8 == 2 or seat_id % 8 == 4:
            print("  ", end="")


if __name__ == "__main__":
    my_seat, id_list = main()
    print_results(id_list, my_seat.id)
    print(f"My seat ID is {my_seat.id}")