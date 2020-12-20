import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    pass


def get_input_sections(input_string):
    rules = []
    messages = []

    for line in input_string.splitlines():
        if not line:
            continue
        if ":" in line:
            rules.append(line)
        else:
            messages.append(line)
    return rules, messages


def rule_factory(rule_string, rule_dict):
    rule_index = int(rule_string.split(":")[0])
    rule_string = rule_string.split(":")[1].strip()

    if '"' in rule_string:

        def func(message):
            if message[:1] == rule_string[1]:
                return True, message[1:]
            return False, message

        rule_dict[rule_index] = func

    else:
        options = rule_string.split(" | ")

        def func(message):
            res = False
            for option in options:
                referenced_rules = option.split()
                new_message = message
                for referenced_rule in referenced_rules:
                    is_valid, new_message = rule_dict[int(referenced_rule)](new_message)
                    if not is_valid:
                        res = False
                        break
                if new_message:
                    res = False
                    break
                else:
                    return True, new_message

        rule_dict[rule_index] = func


if __name__ == "__main__":
    res = main(input_string)
    print(res)