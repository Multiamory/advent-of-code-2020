import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________

NEIGHBORS_TO_CHECK = tuple(
    [
        (x, y, z, w)
        for x in range(-1, 2)
        for y in range(-1, 2)
        for z in range(-1, 2)
        for w in range(-1, 2)
        if (x, y, z, w) != (0, 0, 0, 0)
    ]
)


class Cube:
    def __init__(self, x, y, z, w, char="."):
        self.loc = (x, y, z, w)
        self.state = True if char == "#" else False

    def __add__(self, coords):
        return (
            self.loc[0] + coords[0],
            self.loc[1] + coords[1],
            self.loc[2] + coords[2],
            self.loc[3] + coords[3],
        )

    def __str__(self):
        return f"{self.loc} {self.state}"

    def __repr__(self):
        return "#" if self.state else "."


class Dimension:
    def __init__(self, input_string):
        self.cubes = {}
        for row, chars in enumerate(input_string.splitlines()):
            for col, char in enumerate(chars):
                if char == "#":
                    self.cubes[(row, col, 0, 0)] = Cube(row, col, 0, 0, char)

    def count_active_neighbors(self, loc):
        count = 0
        for neighbor in NEIGHBORS_TO_CHECK:
            coords = tuple(a + b for a, b in zip(loc, neighbor))
            if self[coords].state:
                count += 1
        return count

    def generate_buffer(self):
        return [
            (x, y, z, w)
            for x in range(self.min_x - 1, self.max_x + 2)
            for y in range(self.min_y - 1, self.max_y + 2)
            for z in range(self.min_z - 1, self.max_z + 2)
            for w in range(self.min_w - 1, self.max_w + 2)
        ]

    def evolve(self):
        new_locs = self.generate_buffer()
        new_cubes = {}
        for new_loc in new_locs:
            active_neighbors = self.count_active_neighbors(new_loc)
            if self[new_loc].state and active_neighbors in (2, 3):
                new_cubes[new_loc] = Cube(*new_loc, "#")
            elif not self[new_loc].state and active_neighbors == 3:
                new_cubes[new_loc] = Cube(*new_loc, "#")
        self.cubes = new_cubes

    def __getitem__(self, key):
        if isinstance(key, Cube):
            return self.cubes.get(key.loc, Cube(*key.loc))
        else:
            return self.cubes.get(key, Cube(*key))

    def __repr__(self):
        output = ""
        for w in range(self.min_w, self.max_w + 1):
            output += f"w = {w}\n"
            for z in range(self.min_z, self.max_z + 1):
                output += f"z = {z}\n"
                for x in range(self.min_x, self.max_x + 1):
                    for y in range(self.min_y, self.max_y + 1):
                        if self.cubes.get((x, y, z, w), Cube(0, 0, 0, 0)).state:
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

    @property
    def min_w(self):
        return min(self.cubes.values(), key=lambda c: c.loc[3]).loc[3]

    @property
    def max_w(self):
        return max(self.cubes.values(), key=lambda c: c.loc[3]).loc[3]


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
        print(dimension.count_active_neighbors(cube.loc), end="")
    print()

    print(
        f"Dimension is now {dimension.max_x - dimension.min_x + 1}x{dimension.max_y - dimension.min_y + 1}x{dimension.max_z - dimension.min_z + 1}x{dimension.max_w - dimension.min_w + 1}"
    )
    for i in range(6):
        print(f"Evolution: {i}")
        dimension.evolve()
        print(
            f"Dimension is now {dimension.max_x - dimension.min_x + 1}x{dimension.max_y - dimension.min_y + 1}x{dimension.max_z - dimension.min_z + 1}x{dimension.max_w - dimension.min_w + 1}"
        )

    count = 0
    for cube in dimension.cubes.values():
        if cube.state:
            count += 1

    print(dimension)
    print("total: ", count)
