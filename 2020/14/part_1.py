import sys
import os
import re

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    memory = [0 for _ in range(get_highest_mem(input_string) + 1)]
    mask = "X" * 36

    input_lines = input_string.splitlines()
    for line in input_lines:
        mask, memory = execute_line(line, mask, memory)
    return memory


def execute_line(line, mask, memory):
    if line[0:4] == "mask":
        mask = line.split(" = ")[1]
    else:
        mem_address = int(line.split("]")[0][4:])

        memory[mem_address] = apply_mask_int(int(line.split(" = ")[1]), mask)
    return mask, memory


def apply_mask_int(number, mask):
    bin_num = int_to_bin(number)
    masked_bin = apply_mask_binary(mask, bin_num)
    res = bin_to_int(masked_bin)
    return res


def int_to_bin(number):
    bin_str = bin(number)[2:]
    return bin_str.zfill(36)


def bin_to_int(binary):
    return int(binary, base=2)


def apply_mask_binary(mask, binary):
    assert len(mask) == len(binary)
    res = [
        mask_char if mask_char != "X" else bin_char
        for mask_char, bin_char in zip(mask, binary)
    ]
    return "".join(res)


def get_highest_mem(input_string):
    mem_addresses = [int(mem[1:-1]) for mem in re.findall(r"\[\d+\]", input_string)]
    return max(mem_addresses)


if __name__ == "__main__":
    test_string = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    memory = main(input_string)
    print(memory)

    print(f"Sum = {sum(memory)}")