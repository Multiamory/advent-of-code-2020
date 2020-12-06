import pytest
import part_1
import part_2


@pytest.mark.parametrize(
    "char, expected",
    [
        ("B", [5, 6, 7, 8]),
        ("R", [5, 6, 7, 8]),
        ("F", [1, 2, 3, 4]),
        ("L", [1, 2, 3, 4]),
    ],
)
def test_binary_partition(char, expected):
    res = part_1.partition(char, [1, 2, 3, 4, 5, 6, 7, 8])
    assert res == expected


@pytest.mark.parametrize(
    "char_sequence, expected",
    [
        ("BFFFBBF", 70),
        ("FFFBBBF", 14),
        ("BBFFBBF", 102),
    ],
)
def test_get_row(char_sequence, expected):
    res = part_1.get_row(char_sequence)
    assert res == expected


@pytest.mark.parametrize(
    "char_sequence, expected",
    [
        ("RRR", 7),
        ("LLL", 0),
        ("LLR", 1),
        ("RLR", 5),
        ("RLL", 4),
    ],
)
def test_get_col(char_sequence, expected):
    res = part_1.get_col(char_sequence)
    assert res == expected


@pytest.mark.parametrize(
    "char_sequence, expected",
    [
        ("BFFFBBFRRR", (70, 7, 567)),
        ("FFFBBBFRRR", (14, 7, 119)),
        ("BBFFBBFRLL", (102, 4, 820)),
    ],
)
def test_seat_creator(char_sequence, expected):
    seat = part_1.Seat(char_sequence)
    assert expected == (seat.row, seat.col, seat.id)


@pytest.mark.parametrize(
    "id, expected",
    [
        (567, (70, 7, 567)),
        (119, (14, 7, 119)),
        (820, (102, 4, 820)),
    ],
)
def test_seat_by_id(id, expected):
    seat = part_2.Seat(id)
    assert expected == (seat.row, seat.col, seat.id)