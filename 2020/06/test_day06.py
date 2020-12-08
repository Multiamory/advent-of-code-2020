import pytest

import part_1
import part_2

test_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def test_split_inputs():
    input_list = part_1.split_inputs(test_input)
    assert input_list == ["abc", "abc", "abac", "aaaa", "b"]


def test_split_inputs_2():
    input_list = part_2.split_inputs(test_input)
    assert input_list == [
        ["abc"],
        ["a", "b", "c"],
        ["ab", "ac"],
        ["a", "a", "a", "a"],
        ["b"],
    ]


def test_eliminate_letters():
    input_list = part_2.split_inputs(test_input)
    og_letters = part_2.count_shared_answers(input_list[2])
    print(og_letters)
    assert og_letters == 1


def test_main():
    count = part_2.main(
        """necytxmlfhsu
uecosjvlhpmk

mnslbuziphawkxyg
whpmnesikaglzb

kaw
akw

qurg
hrqug
qrgu
gruq

sczomkv
zejkhvslmucbwdo
pxsianovzcmk
tcokmvsyz
ozskvimcr

tfzajkxngwsqrbleic
tijoqnerxsplwzgabkfc
ogkezbiwqtaxrscljfn
xsqauezwnjckbtgiryfdml"""
    )
    assert count == 6