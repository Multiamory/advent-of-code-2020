import part_2

import pytest


@pytest.mark.parametrize(
    "input_string,result",
    [
        ("7,13,x,x,59,x,31,19", 1068781),
        ("17,x,13,19", 3417),
        ("67,7,59,61", 754018),
        ("67,x,7,59,61", 779210),
        ("67,7,x,59,61", 1261476),
        ("1789,37,47,1889", 1202161486),
    ],
)
def test_part2(input_string, result):
    res = part_2.main(input_string)
    assert res == result


def test_highest_buses():
    buses = [part_2.Bus(i, n) for i, n in enumerate([1, 5, 8, 12, 4, 25, 99, 2, "x"])]
    highest = part_2.get_highest_buses(buses, 3)
    print(highest)
    assert 0