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
    input_lines = input_string.splitlines()

    highest_mem = get_highest_mem(input_string)
    most_Xs = get_max_Xs(input_lines)
    highest_mem = (2 ** most_Xs) + highest_mem

    memory = {}

    mask = "0" * 36

    total_lines = len(input_lines)
    for i, line in enumerate(input_lines):
        print(i, flush=True)
        # print(f"{i/total_lines}%", flush=True)
        mask, memory = execute_line(line, mask, memory)
    return memory


def execute_line(line, mask, memory):
    if line[0:4] == "mask":
        mask = line.split(" = ")[1]
    else:
        number = int(line.split(" = ")[1])
        initial_address = int_to_bin(int(line.split("]")[0][4:]))
        mem_addresses = apply_mask_v2(initial_address, mask)
        for mem_address in mem_addresses:
            memory[bin_to_int(mem_address)] = number
    return mask, memory


def apply_mask_v2(bin_num, mask):
    assert len(bin_num) == len(mask)
    results = ["".join([m if m != "0" else b for b, m in zip(bin_num, mask)])]
    return apply_mask_recursive(results)


def apply_mask_recursive(list_of_bins):
    new_list = []
    for b in list_of_bins:
        if "X" in b:
            new_list.append(b.replace("X", "0", 1))
            new_list.append(b.replace("X", "1", 1))
    if not new_list:
        return list_of_bins
    else:
        return apply_mask_recursive(new_list)


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


def get_max_Xs(lines):
    highest_Xs = 0
    for line in lines:
        if line.count("X") > highest_Xs:
            highest_Xs = line.count("X")

    return highest_Xs


if __name__ == "__main__":
    test_string = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

    print(bin_to_int("1" * 36))

    memory = main(input_string)
    # print(memory)

    print(f"Sum = {sum(memory.values())}")