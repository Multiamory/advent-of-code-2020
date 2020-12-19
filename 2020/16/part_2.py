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
    print("Rules: ", rules)
    valid_tickets = []
    for ticket in nearby_tickets:
        if ticket_is_valid_part1(ticket, rules):
            valid_tickets.append(ticket)

    print("Valid Tickets:", valid_tickets)
    possible_field_list = collect_valid_fields(valid_tickets, rules)
    print(possible_field_list)
    possible_field_list = narrow_down_fields(possible_field_list)
    print(possible_field_list)

    total_product = 1
    print("Processing my ticket.")
    for field, number in enumerate(my_ticket[0].split(",")):
        print(f"Field {field}: {number}")
        number = int(number)
        field_name = list(possible_field_list[field])[0]
        if "departure" in field_name:
            print(f"Adding {field_name} = {number} to total.")
            total_product *= number

    return total_product


def narrow_down_fields(possible_field_list):
    print("Narrowing fields")
    for i in range(len(possible_field_list)):
        if len(possible_field_list[i]) == 1:
            for k in range(len(possible_field_list)):
                if k == i:
                    continue
                possible_field_list[k] = possible_field_list[k] - possible_field_list[i]
    if all([len(field) == 1 for field in possible_field_list]):
        return possible_field_list
    else:
        return narrow_down_fields(possible_field_list)


def collect_valid_fields(valid_tickets, rules):
    fields = [set([label[0] for label in rules]) for _ in rules]
    for ticket in valid_tickets:
        for field, number in enumerate(ticket.split(",")):
            number = int(number)
            valid_rules = check_number(number, rules)
            fields[field] = fields[field] & valid_rules
    return fields


def ticket_is_valid_part1(ticket_string, rules):
    ticket_status = True
    for number in ticket_string.split(","):
        number = int(number)
        if not check_number(number, rules):
            ticket_status = False
    return ticket_status


def check_number(number, rules):
    valid_rules = []
    for rule in rules:
        if validate_rule(number, rule):
            valid_rules.append(rule)
    return set([label[0] for label in valid_rules])


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
    test_string = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,13,12

nearby tickets:
3,18,9
15,5,1
5,9,14"""

    res = main(input_string)
    print(f"Total departure fields: {res}")