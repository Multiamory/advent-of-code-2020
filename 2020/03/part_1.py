import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main():
    matrix = Matrix(input_string)
    index = Index(0, 0, matrix)
    total_trees = main_loop(matrix, index)
    print(f"We hit {total_trees} trees!")


def main_loop(matrix, index):
    total_trees = 0
    while True:
        try:
            char = matrix.get_char_at_index(index)
            print_line(matrix, index)
            if char == "#":
                total_trees += 1
            index = index.move(3, 1)
        except EndOfPuzzle:
            print("We reached the end!")
            break
    return total_trees


def print_line(matrix, index):
    line = matrix.matrix[index.y]
    char = line[index.real_x]
    line[index.real_x] = "\033[41mX\033[0m" if char == "#" else "\033[42mX\033[0m"
    print("".join(line))


class Matrix:
    def __init__(self, input_string):
        self.matrix = createMatrix(input_string)
        self.width = len(self.matrix[0])
        self.height = len(self.matrix)

    def get_char_at_index(self, index):
        assert index.real_x <= self.width
        if index.y >= self.height:
            raise EndOfPuzzle("You reached the end!")
        return self.matrix[index.y][index.real_x]

    def __repr__(self):
        result = ""
        for row in self.matrix:
            result += "{}\n".format("".join(row))

        return result


def createMatrix(input_string):
    input_lines = input_string.splitlines()
    tree_matrix = [[char for char in line] for line in input_lines]
    return tree_matrix


class Index:
    def __init__(self, x, y, matrix):
        self.x = x
        self.real_x = x % matrix.width
        self.y = y
        self.matrix = matrix

    def move(self, x, y):
        new_x = self.x + x
        new_y = self.y + y
        return Index(new_x, new_y, self.matrix)

    def __repr__(self):
        return f"Index({self.x},{self.y}) real x: {self.real_x}"


class EndOfPuzzle(Exception):
    pass


if __name__ == "__main__":
    main()