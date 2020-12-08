sample_rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

import part_1
import part_2


def test_bag_init():
    input_lines = sample_rules.splitlines()
    bag = part_1.Bag(input_lines[0])

    assert bag.type == "light red"


def test_bag_methods():
    input_lines = sample_rules.splitlines()
    bag1 = part_1.Bag(input_lines[0])
    bag2 = part_1.Bag(input_lines[1])
    bag3 = part_1.Bag(input_lines[2])

    bag1.add_contains([bag2, bag2, bag2, bag3])
    bag2.add_contains(
        [
            bag3,
        ]
    )

    assert bag1.contains == [bag2, bag2, bag2, bag3]
    assert bag2.contained_in == {
        bag1,
    }
    assert bag3.contained_in == {bag1, bag2}


def test_baggage_claim():
    input_lines = sample_rules.splitlines()

    bags = part_1.Baggage_Claim()
    bags["test bag"]
    bags["test bag"]

    print(bags)
    assert bags.bags == {"test bag": part_1.Bag("test bag")}


def test_parse_line():
    input_lines = sample_rules.splitlines()

    bags = part_1.Baggage_Claim()

    bags.parse_line(input_lines[0])

    print(bags)
    assert len(bags.bags) == 3
    assert bags["bright white"].contained_in == {part_1.Bag("light red")}
    assert len(bags["light red"].contains) == 3


def test_main():
    res = part_1.main(sample_rules)
    print(res)

    assert len(res) == 4