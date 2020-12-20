import part_1

test_input = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""


def test_get_inputs():
    rules, messages = part_1.get_input_sections(test_input)
    assert rules == [
        "0: 4 1 5",
        "1: 2 3 | 3 2",
        "2: 4 4 | 5 5",
        "3: 4 5 | 5 4",
        '4: "a"',
        '5: "b"',
    ]
    assert messages == ["ababbb", "bababa", "abbbab", "aaabbb", "aaaabbb"]


def test_simple_rule():
    rules = {}
    part_1.rule_factory('0: "a"', rules)
    isValid, remaining = rules[0]("a")
    assert isValid and remaining == ""
    isValid, remaining = rules[0]("abb")
    assert isValid and remaining == "bb"


def test_rule_reference():
    rules = {}
    part_1.rule_factory('1: "a"', rules)
    part_1.rule_factory('2: "b"', rules)
    part_1.rule_factory("0: 1 2", rules)
    print(rules)
    isValid, remaining = rules[0]("ab")
    assert isValid and remaining == ""
    isValid, remaining = rules[0]("a")
    assert not isValid and remaining == ""
    isValid, remaining = rules[0]("abb")
    assert not isValid and remaining == "b"


def test_rule_with_pipe():
    rules = {}
    part_1.rule_factory('1: "a"', rules)
    part_1.rule_factory('2: "b"', rules)
    part_1.rule_factory("0: 1 2 | 2 1", rules)
    print(rules)
    isValid, remaining = rules[0]("ab")
    assert isValid and remaining == ""
    isValid, remaining = rules[0]("ba")
    assert isValid and remaining == ""
    isValid, remaining = rules[0]("abb")
    assert not isValid and remaining == "b"
    isValid, remaining = rules[0]("b")
    assert not isValid and remaining == ""
