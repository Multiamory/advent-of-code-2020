import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    rule_strings, messages = get_input_sections(input_string)
    rules = create_rule_dict(rule_strings)
    count = 0
    for message in messages:
        if check_rule(message, rules[0], rules) == "":
            count += 1
    return count


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


def create_rule_dict(rules):
    rule_dict = {}
    for rule in rules:
        rule_index = int(rule.split(":")[0])
        rule_string = rule.split(":")[1].strip()
        rule_dict[rule_index] = rule_string
    return rule_dict


def check_rule(message, rule_string, rules):
    # print("Rule: {}".format(rule_string))

    if '"' in rule_string:
        if message[:1] == rule_string[1]:
            return message[1:]
        return False

    elif "|" not in rule_string:
        referenced_rules = rule_string.split()
        for referenced_rule in referenced_rules:
            message = check_rule(message, rules[int(referenced_rule)], rules)
            if message is False:
                return False

        return message

    else:
        options = rule_string.split(" | ")
        for option in options:
            new_message = check_rule(message, option, rules)
            if new_message is not False:
                return new_message
        return False


if __name__ == "__main__":
    res = main(input_string)
    print(res)