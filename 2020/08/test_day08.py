sample_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

import urwid

palette = [
    ("banner", "black", "light gray"),
    ("streak", "black", "dark red"),
    ("bg", "black", "dark blue"),
    ("reversed", "standout", ""),
]


def main():
    lines = input_string.splitlines()[:20]
    code_lines = [CodeLine(line) for line in lines]
    l_box = urwid.ListBox(urwid.SimpleListWalker(code_lines))

    loop = urwid.MainLoop(l_box, palette, unhandled_input=exit_on_q)
    loop.run()


class CodeLine(urwid.AttrMap):
    def __init__(self, line):
        t_line = urwid.Text(line)
        super(CodeLine, self).__init__(t_line, None, focus_map="reversed")


def exit_on_q(key):
    if key in ("q", "Q"):
        exit_program()


def exit_program():
    raise urwid.ExitMainLoop()


if __name__ == "__main__":
    main()