import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________

NEIGHBORS_TO_CHECK = (
    (-1, -1, -1),
    (-1, -1, 0),
    (-1, -1, 1),
    (-1, 0, -1),
    (-1, 0, 0),
    (-1, 0, 1),
    (-1, 1, -1),
    (-1, 1, 0),
    (-1, 1, 1),
    (0, -1, -1),
    (0, -1, 0),
    (0, -1, 1),
    (0, 0, -1),
    (0, 0, 1),
    (0, 1, -1),
    (0, 1, 0),
    (0, 1, 1),
    (1, -1, -1),
    (1, -1, 0),
    (1, -1, 1),
    (1, 0, -1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, -1),
    (1, 1, 0),
    (1, 1, 1),
)


class Cube:
    def __init__(self, x, y, z, char="."):
        self.loc = (x, y, z)
        self.state = True if char == "#" else False

    def __add__(self, coords):
        return (
            self.loc[0] + coords[0],
            self.loc[1] + coords[1],
            self.loc[2] + coords[2],
        )

    def __repr__(self):
        return str(self.loc)


class Dimension:
    def __init__(self, input_string):
        self.cubes = {}
        for row, chars in enumerate(input_string.splitlines()):
            for col, char in enumerate(chars):
                self.cubes[(row, col, 0)] = Cube(row, col, 0, char)

    def count_active_neighbors(self, cube):
        count = 0
        for neighbor in NEIGHBORS_TO_CHECK:
            if self.cubes.get(cube + neighbor, Cube(0, 0, 0)).state:
                count += 1
        return count

    def generate_buffer(self):
        outer_layer = set()
        for x in range(self.min_x - 1, self.max_x + 2):
            for y in range(self.min_y - 1, self.max_y + 2):
                for z in range(self.min_z - 1, self.max_z + 2):
                    outer_layer.add(Cube(x, y, z))

        return outer_layer

    def evolve(self):
        new_cubes = self.generate_buffer()
        for new_cube in new_cubes:
            active_neighbors = self.count_active_neighbors(new_cube)
            if self[new_cube].state and active_neighbors in (2, 3):
                new_cube.state = True
            elif not self[new_cube].state and active_neighbors == 3:
                new_cube.state = True
        for new_cube in new_cubes:
            self.cubes[new_cube.loc] = new_cube

    def __getitem__(self, key):
        if isinstance(key, Cube):
            return self.cubes.get(key.loc, Cube(*key.loc))
        else:
            return self.cubes.get(key, Cube(*key))

    def __repr__(self):
        output = ""
        for z in range(self.min_z, self.max_z + 1):
            output += f"z = {z}\n"
            for x in range(self.min_x, self.max_x + 1):
                for y in range(self.min_y, self.max_y + 1):
                    if self.cubes[(x, y, z)].state:
                        output += "#"
                    else:
                        output += "."
                output += "\n"
        return output

    @property
    def min_x(self):
        return min(self.cubes.values(), key=lambda c: c.loc[0]).loc[0]

    @property
    def max_x(self):
        return max(self.cubes.values(), key=lambda c: c.loc[0]).loc[0]

    @property
    def min_y(self):
        return min(self.cubes.values(), key=lambda c: c.loc[1]).loc[1]

    @property
    def max_y(self):
        return max(self.cubes.values(), key=lambda c: c.loc[1]).loc[1]

    @property
    def min_z(self):
        return min(self.cubes.values(), key=lambda c: c.loc[2]).loc[2]

    @property
    def max_z(self):
        return max(self.cubes.values(), key=lambda c: c.loc[2]).loc[2]


if __name__ == "__main__":
    test_string = """.#.
..#
###"""
    dimension = Dimension(input_string)
    row = 0
    print(dimension)

    for cube in dimension.cubes.values():
        if cube.loc[0] != row:
            print()
            row = cube.loc[0]
        print(dimension.count_active_neighbors(cube), end="")
    print()

    for _ in range(6):
        dimension.evolve()

    count = 0
    for cube in dimension.cubes.values():
        if cube.state:
            count += 1

    print(dimension)
    print("total: ", count)
