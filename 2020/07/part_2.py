import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    baggage_claim = Baggage_Claim()
    input_lines = input_string.splitlines()
    for line in input_lines:
        baggage_claim.parse_line(line)

    results = count_children(baggage_claim["shiny gold"])
    return results


def get_ancestors(bag):
    results = set()
    for parent in bag.contained_in:
        results.add(parent)
        results |= get_ancestors(parent)
    return results


def count_children(bag, indent=""):
    results = 0
    for child in bag.contains:
        results += 1
        results += count_children(child, indent=indent + "  ")

    return results


class Baggage_Claim:
    def __init__(self):
        self.bags = {}

    def parse_line(self, line):
        main_bag, child_string = line.split("bags contain")
        self[main_bag]

        child_string = (
            child_string.replace(".", "").replace("bags", "").replace("bag", "")
        )
        child_bags = child_string.split(",")
        for child_bag in child_bags:
            if "no other" in child_bag:
                continue
            number = int(child_bag.split()[0])
            name = " ".join(child_bag.split()[1:])
            self[main_bag].add_contains([self[name] for x in range(number)])

    def __getitem__(self, name):
        name = name.strip()
        if name not in self.bags:
            self.bags[name] = Bag(name)
        return self.bags[name]

    def __repr__(self):
        return f"Baggage_Claim({', '.join(self.bags.keys())})"


class Bag:
    def __init__(self, bag_line):
        bag_description = bag_line.split("bags contain")[0].strip()
        self.type = bag_description
        self.contains = []
        self.contained_in = set()

    def add_contains(self, children):
        self.contains += children
        for child in children:
            child.add_contained_in(self)

    def add_contained_in(self, parent):
        self.contained_in.add(parent)

    def __eq__(self, other):
        if isinstance(other, Bag) and other.type == self.type:
            return True
        return False

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        return self.type


if __name__ == "__main__":
    res = main(input_string)

    print(res)