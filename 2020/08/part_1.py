import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    acc = 0
    position = 0
    commands = [[line, False] for line in input_string.splitlines()]

    while True:
        print(f"[Acc={str(acc).rjust(4)}] Line {position}: {commands[position]}")
        try:
            acc, position = do_command(commands[position], acc, position)
        except DuplicateCommand:
            break

    return acc


class DuplicateCommand(Exception):
    pass


def do_command(command, acc, position):
    if command[1]:
        raise DuplicateCommand()
    command[1] = True
    parts = command[0].split()
    if parts[0] == "nop":
        return acc, position + 1
    if parts[0] == "acc":
        return acc + int(parts[1]), position + 1
    if parts[0] == "jmp":
        return acc, position + int(parts[1])


if __name__ == "__main__":
    test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    res = main(input_string)
    print("\n\nResult: ", res)