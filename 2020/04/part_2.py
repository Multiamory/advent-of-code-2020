import sys
import os
from collections import defaultdict
import re

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


FIELDS = ["eyr", "iyr", "hcl", "byr", "ecl", "hgt", "pid", "cid"]


def split_inputs(input_string):
    lines = input_string.splitlines()
    input_list = []
    current_item = ""
    for line in lines:
        if line:
            current_item += " {}".format(line)
        else:
            input_list.append(current_item.strip())
            current_item = ""
    if current_item not in input_list:
        input_list.append(current_item.strip())
    return input_list


def convert_to_dict(string_item):
    result = {}
    for item in string_item.split():
        k, v = item.split(":")
        result[k] = v

    return result


class Passport:
    def __init__(self, input_dict):
        for field in FIELDS:
            self.__setattr__(field, input_dict.get(field, None))

    def isValid(self):
        for field in FIELDS:
            if not self.isValidValue(field):
                return False
        return True

    def isValidValue(self, key):
        value = self[key]
        if key == "cid":
            return True
        elif not value:
            return False
        elif key == "byr":
            if len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
                return True
        elif key == "iyr":
            if len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
                return True
        elif key == "eyr":
            if len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
                return True
        elif key == "ecl":
            if value in [
                "amb",
                "blu",
                "brn",
                "gry",
                "grn",
                "hzl",
                "oth",
            ]:
                return True
        elif key == "pid":
            if len(value) == 9 and re.match("^[0-9]+$", value):
                return True
        elif key == "hcl":
            if len(value) == 7 and re.match("^[#0-9a-f]+$", value):
                return True
        elif key == "hgt":
            if "cm" in value:
                if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                    return True
            elif "in" in value:
                if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                    return True
        return False

    def red(self, string):
        return f"\u001b[31m{string}\u001b[0m"

    def item_str(self, key):
        if key == "cid":
            return f"{key}: {self[key]}".ljust(15)
        else:
            if self.isValidValue(key):
                return f"{key}: {self[key]}".ljust(15)
            else:
                return f"{key}: {self.red(self[key])}".ljust(15 + len(self.red("")))

    def __getitem__(self, key):
        return self.__getattribute__(key)

    def __iter__(self):
        return [self[field] for field in FIELDS]

    def __repr__(self):
        return " ".join([self.item_str(field) for field in FIELDS])


if __name__ == "__main__":
    entries = split_inputs(input_string)
    passports = [Passport(convert_to_dict(entry)) for entry in entries]
    count = 0
    for passport in passports:
        if passport.isValid():
            count += 1
            print(str(count).ljust(4), passport)
        else:
            print("".ljust(4), passport)