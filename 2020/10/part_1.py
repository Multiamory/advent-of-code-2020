import sys
import os

# ___________ Begin Setup and Get Input _____________
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import get_input

# This is the input for the day's puzzle
input_string = get_input.get_input_for_day(__file__)
# __________________ End of setup ____________________


def main(input_string):
    input_values = tuple(int(n) for n in input_string.splitlines())
    sorted_inputs = sorted(input_values)
    sorted_inputs.append(sorted_inputs[-1] + 3)
    print(sorted_inputs)
    jolt_diffs = get_jolt_gaps(sorted_inputs)
    print(f"{jolt_diffs[0]} one-jolt diffs and {jolt_diffs[1]} three-jolt diffs")
    return jolt_diffs[1] * jolt_diffs[0]


def get_jolt_gaps(sorted_inputs):
    jolts = 0
    jolt_diffs = [0, 0]
    for adapter in sorted_inputs:
        jolts_diff = adapter - jolts
        if jolts_diff > 3:
            raise Exception("The difference is too large")
        jolt_diffs[(adapter - jolts - 1) // 2] += 1
        jolts = adapter
    print(f"returning {jolt_diffs}")
    return jolt_diffs


if __name__ == "__main__":
    test_input = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

    res = main(input_string)
    print(f"The result is {res}")