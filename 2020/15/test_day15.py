import part_1
import part_2_v2
import pytest


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("1,3,2", 1),
        ("2,1,3", 10),
        ("1,2,3", 27),
        ("2,3,1", 78),
        ("3,2,1", 438),
        ("3,1,2", 1836),
    ],
)
def test_part1(input_string, expected):
    assert part_1.main(input_string) == expected


@pytest.mark.parametrize(
    "input_string,expected",
    [
        ("0,3,6", 175594),
        ("1,3,2", 2578),
        ("2,1,3", 3544142),
        ("1,2,3", 261214),
        ("2,3,1", 6895259),
        ("3,2,1", 18),
        ("3,1,2", 362),
    ],
)
def test_part2(input_string, expected):
    assert part_2_v2.main(input_string) == expected