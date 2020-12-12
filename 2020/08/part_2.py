import sys
import os
import copy

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):

    commands = [
        [index, line, False] for index, line in enumerate(input_string.splitlines())
    ]
    _, visited_commands, _ = run_commands(copy.deepcopy(commands))

    sorted_commands = sorted(
        visited_commands, key=lambda command: command[0], reverse=True
    )

    for command in sorted_commands:
        edited_commands = copy.deepcopy(commands)
        if "jmp" in command[1]:
            print(f"Editing {command} to nop")
            edited_commands[command[0]][1] = edited_commands[command[0]][1].replace(
                "jmp", "nop"
            )
        elif "nop" in command[1]:
            print(f"Editing {command} to jmp")
            edited_commands[command[0]][1] = edited_commands[command[0]][1].replace(
                "nop", "jmp"
            )
        else:
            continue
        acc, _, reachedEnd = run_commands(edited_commands)
        if reachedEnd:
            return acc


def run_commands(commands):
    visited_commands = []
    acc = 0
    position = 0
    while True:
        print(f"[Acc={str(acc).rjust(4)}] Line {position}: {commands[position]}")
        try:
            acc, position = do_command(commands[position], acc, position)
            visited_commands.append(commands[position])
        except DuplicateCommand:
            return acc, visited_commands, False
        except IndexError:
            print("We got to the end!")
            return acc, visited_commands, True
    raise Exception("We should have hit a duplicate or the end...")


class DuplicateCommand(Exception):
    pass


def do_command(command, acc, position):
    if command[2]:
        raise DuplicateCommand()
    command[2] = True
    parts = command[1].split()
    if parts[0] == "nop":
        return acc, position + 1
    if parts[0] == "acc":
        return acc + int(parts[1]), position + 1
    if parts[0] == "jmp":
        return acc, position + int(parts[1])


if __name__ == "__main__":
    res = main(input_string)
    print("\n\nResult: ", res)