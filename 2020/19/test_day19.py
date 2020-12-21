import part_1
import part_2

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
    rules = part_1.create_rule_dict(['0: "a"'])
    res = part_1.check_rule("a", rules[0], rules)
    assert res == ""
    res = part_1.check_rule("bb", rules[0], rules)
    assert res is False
    res = part_1.check_rule("abb", rules[0], rules)
    assert res == "bb"


def test_rule_reference():
    rules = part_1.create_rule_dict(
        [
            '1: "a"',
            '2: "b"',
            "0: 1 2",
        ]
    )
    res = part_1.check_rule("ab", rules[0], rules)
    assert res == ""
    res = part_1.check_rule("a", rules[0], rules)
    assert res is False
    res = part_1.check_rule("abb", rules[0], rules)
    assert res == "b"


def test_or_rules():
    rules = part_1.create_rule_dict(
        [
            '1: "a"',
            '2: "b"',
            "0: 1 2 | 2 1",
        ]
    )
    res = part_1.check_rule("ab", rules[0], rules)
    assert res == ""
    res = part_1.check_rule("ba", rules[0], rules)
    assert res == ""
    res = part_1.check_rule("abb", rules[0], rules)
    assert res == "b"
    res = part_1.check_rule("bb", rules[0], rules)
    assert res is False


def test_main():
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
    res = part_1.main(test_input)
    print(res)
    assert res == 2


def test_main_part1():
    test_input = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""
    res = part_1.main(test_input)
    assert res == 3


def test_p2_simple_rule():
    rules = part_2.create_rule_dict(['0: "a"'])
    res = part_2.check_rule("a", rules[0], rules)
    assert res == ""
    res = part_2.check_rule("bb", rules[0], rules)
    assert res is False
    res = part_2.check_rule("abb", rules[0], rules)
    assert res == "bb"


def test_p2_rule_reference():
    rules = part_2.create_rule_dict(
        [
            '1: "a"',
            '2: "b"',
            "0: 1 2",
        ]
    )
    res = part_2.check_rule("ab", rules[0], rules)
    assert res == ""
    res = part_2.check_rule("a", rules[0], rules)
    assert res is False
    res = part_2.check_rule("abb", rules[0], rules)
    assert res == "b"


def test_p2_or_rules():
    rules = part_1.create_rule_dict(
        [
            '1: "a"',
            '2: "b"',
            "0: 1 2 | 2 1",
        ]
    )
    res = part_2.check_rule("ab", rules[0], rules)
    assert res == ""
    res = part_2.check_rule("ba", rules[0], rules)
    assert res == ""
    res = part_2.check_rule("abb", rules[0], rules)
    assert res == "b"
    res = part_2.check_rule("bb", rules[0], rules)
    assert res is False


def test_p2_main():
    test_input = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""
    res = part_2.main(test_input)
    assert res == 12
