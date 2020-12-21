import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


class Printer:
    def __init__(self):
        self.indent = 0

    def print(self, text):
        print("  " * self.indent + text)


p = Printer()


def main(input_string):
    rule_strings, messages = get_input_sections(input_string)
    rules = create_rule_dict(rule_strings)
    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"
    count = 0
    for key in sorted(rules.keys()):
        p.print(f"{key}: {rules[key]}")
    approved = []
    for message in messages:
        p.print(f"Original Message: {message}")
        if check_rule(message, 0, rules) == "":
            count += 1
            approved.append(message)
            p.print(message)
    for m in approved:
        print(m)
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
    if isinstance(rule_string, int):
        p.print(f"{message} -> {rule_string}: {rules[rule_string]}")
        rule_string = rules[rule_string]
    else:
        p.print(f"{message} -> {rule_string}")

    if '"' in rule_string:
        if message[:1] == rule_string[1]:
            return message[1:]
        p.print(f"Char {message[:1]} does not match {rule_string[1]}")
        return False

    elif "|" not in rule_string:
        p.print("Checking two rules")
        referenced_rules = rule_string.split()
        p.indent += 1
        for referenced_rule in referenced_rules:
            message = check_rule(message, int(referenced_rule), rules)
            if message is False:
                p.indent -= 1
                return False
        p.indent -= 1
        return message

    else:
        p.print("Checking OR rules:")
        options = rule_string.split(" | ")
        p.indent += 1
        for option in options:
            p.print(f"-Rule {option}")
            new_message = check_rule(message, option, rules)
            if new_message is not False:
                p.indent -= 1
                return new_message
        p.indent -= 1
        p.print("Neither option passed")
        return False


if __name__ == "__main__":
    test_input = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

babbbbaabbbbbabbbbbbaabaaabaaa"""
    res = main(test_input)
    # res = main(input_string)
    p.print(str(res))