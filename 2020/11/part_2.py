import sys
import os
import copy

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________

spaces_to_check = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def main(input_string):
    input_rows = input_string.splitlines()
    seating = Seating(input_rows)
    iteration_count = 0
    while True:
        try:
            seating.update_seating()
            print_seating(seating)
        except NoChange:
            print("--------No Change Detected!---------")
            break
    return seating


class Seating:
    def __init__(self, input_rows):
        self.matrix = [[col for col in row] for row in input_rows]
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    def count_occupied_seats(self):
        occupied_count = 0
        for seat in iterate_seat_coords(self.matrix):
            if self.is_seat(seat) and self.is_occupied(seat):
                occupied_count += 1
        return occupied_count

    def update_seating(self):
        new_seating = copy.deepcopy(self.matrix)
        for seat in iterate_seat_coords(new_seating):
            if not self.is_seat(seat):
                continue
            neighbors = self.count_neighbors(seat)
            if self.is_occupied(seat) and neighbors >= 5:
                new_seating[seat[0]][seat[1]] = "L"
            elif not self.is_occupied(seat) and neighbors == 0:
                new_seating[seat[0]][seat[1]] = "#"
        if self.matrix == new_seating:
            raise NoChange
        self.matrix = new_seating

    def count_neighbors(self, row_col):
        occupied_neighbors = 0
        for neighbor in spaces_to_check:
            multiplier = 1
            while True:
                space_to_check = tuple(
                    a + (b * multiplier) for a, b in zip(row_col, neighbor)
                )
                if (
                    space_to_check[0] < 0
                    or space_to_check[0] > len(self.matrix) - 1
                    or space_to_check[1] < 0
                    or space_to_check[1] > len(self.matrix[0]) - 1
                ):
                    break
                if self.is_seat(space_to_check):
                    if self.is_occupied(space_to_check):
                        occupied_neighbors += 1
                    break
                multiplier += 1

        return occupied_neighbors

    def is_occupied(self, row_col):
        status = self.matrix[row_col[0]][row_col[1]]
        if status == "#":
            return True
        return False

    def is_seat(self, row_col):
        status = self.matrix[row_col[0]][row_col[1]]
        if status in ["L", "#"]:
            return True
        return False


def iterate_seat_coords(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            yield (row, col)


def print_seating(seating):
    print("_" * len(seating.matrix[0]))
    for row in seating.matrix:
        print("".join(row))


class NoChange(Exception):
    pass


if __name__ == "__main__":
    test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

    res = main(input_string)
    print(f"Empty seats: {res.count_occupied_seats()}")
