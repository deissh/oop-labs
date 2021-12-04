import re
from typing import List

order = {
    '+': 0,
    '-': 0,
    '/': 1,
    '*': 1,
    '^': 2,
    '(': 3,
    ')': 3,
}

exp_re = re.compile(r'(\d+|[^ 0-9])')


def rpn_convert(exp: str) -> str:
    tokens = re.findall(exp_re, exp)
    tokens = [t for t in reversed(tokens) if t != '']

    def parser(raw: List[str], op):
        rpn = ''
        sstr = raw.copy()
        if sstr.pop() == '(':

            while len(sstr) > 0:
                if sstr.pop() == ')':
                    rpn += " " + parser(raw[(len(sstr)+1):][:-1], 0)
        else:
            rpn = raw.pop()

        while len(raw) > 0:
            curr = order[raw[-1]]
            if curr < op:
                break

            op = raw.pop()

            arg2 = parser(raw, curr + 1)
            rpn += " " + arg2 + " " + op
        return rpn

    return parser(tokens, 0)


if __name__ == '__main__':
    expression = input('# ')

    print(f"rpn={rpn_convert(expression)}")
