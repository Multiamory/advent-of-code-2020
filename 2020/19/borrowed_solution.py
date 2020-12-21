#!/usr/bin/env python
"""
I had a really hard time with this so I found this solution at
https://github.com/viliampucik/adventofcode/blob/master/2020/19.py

It is so beautiful and efficient I'm in awe. The way the expand function
creates this one huge regex is awesome.
"""


import sys
import regex
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)

# Kudos to https://github.com/taddeus/advent-of-code/blob/master/2020/19_regex.py
def solve(rules, messages):
    def expand(value):
        if not value.isdigit():
            return value
        return "(?:" + "".join(map(expand, rules[value].split())) + ")"

    r = regex.compile(expand("0"))
    print(r)
    return sum(r.fullmatch(m) is not None for m in messages)


raw_rules, messages = input_string.split("\n\n")
messages = messages.splitlines()
rules = dict(
    raw_rule.replace('"', "").split(": ", 1) for raw_rule in raw_rules.splitlines()
)

print(solve(rules, messages))
rules["8"] = "42 +"  # repeat pattern
rules["11"] = "(?P<R> 42 (?&R)? 31 )"  # recursive pattern
print(solve(rules, messages))