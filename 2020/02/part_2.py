import sys
import os
from collections import namedtuple

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________

PasswordPair = namedtuple("PasswordPair", ["policy", "password"])


class Policy:
    def __init__(self, policy_string):
        policy_parts = policy_string.split(" ")
        self.char = policy_parts[1]
        self.index_a = int(policy_parts[0].split("-")[0]) - 1
        self.index_b = int(policy_parts[0].split("-")[1]) - 1

    def test_password(self, password):
        password = password.strip()
        is_char_a = password[self.index_a] == self.char
        is_char_b = password[self.index_b] == self.char

        return is_char_a != is_char_b

    def __repr__(self):
        return f"{self.char}: {self.min}-{self.max}"


def main():
    input_tuples = tuple(
        [
            PasswordPair(Policy(line.split(":")[0]), line.split(":")[1])
            for line in input_string.splitlines()
        ]
    )
    print(f"Total valid password: {count_correct(input_tuples)}")


def count_correct(input_tuples):
    count = 0
    for input_tuple in input_tuples:
        if input_tuple.policy.test_password(input_tuple.password):
            count += 1

    return count


if __name__ == "__main__":
    main()