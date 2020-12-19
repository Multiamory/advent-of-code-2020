import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    rules_strings, my_ticket, nearby_tickets = separate_inputs(input_string)
    rules = parse_rules(rules_strings)
    print(rules)
    invalid_numbers = []
    for ticket in nearby_tickets:
        print(ticket_is_valid_part1(ticket, rules, invalid_numbers), ticket)

    return invalid_numbers


def ticket_is_valid_part1(ticket_string, rules, invalid_numbers):
    ticket_status = True
    for number in ticket_string.split(","):
        print(f"checking {number}")
        number = int(number)
        if not check_number(number, rules):
            invalid_numbers.append(number)
            ticket_status = False
    return ticket_status


def check_number(number, rules):
    for rule in rules:
        if validate_rule(number, rule):
            return True
    return False


def validate_rule(number, rule):
    if number >= rule[1][0] and number <= rule[1][1]:
        return True
    if number >= rule[2][0] and number <= rule[2][1]:
        return True
    return False


def parse_rules(rules_strings):
    rules = []
    for rule in rules_strings:
        parts = rule.split(": ")
        label = parts[0].strip()
        first_range = [int(num) for num in parts[1].split(" or ")[0].split("-")]
        second_range = [int(num) for num in parts[1].split(" or ")[1].split("-")]

        rules.append((label, first_range, second_range))
    return rules


def separate_inputs(input_string):
    lines = input_string.splitlines()
    rules = []
    my_ticket = []
    nearby_tickets = []
    current_section = rules
    for line in lines:
        if not line:
            continue
        if line == "your ticket:":
            current_section = my_ticket
            continue
        if line == "nearby tickets:":
            current_section = nearby_tickets
            continue
        current_section.append(line)
    return rules, my_ticket, nearby_tickets


if __name__ == "__main__":
    test_string = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

    res = main(input_string)
    print("Invalid Numbers: ", res)
    print(f"Sum total: {sum(res)}")