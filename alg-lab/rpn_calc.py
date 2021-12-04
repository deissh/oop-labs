import operator

operators = {
    '+': [operator.add, 2],
    '-': [operator.sub, 2],
    '*': [operator.mul, 2],
    '/': [operator.truediv, 2],
    '^': [operator.pow, 2],
    '%': [operator.mod, 2],
    '<<': [operator.lshift, 2],
    '>>': [operator.rshift, 2],
}


def error_string(token, values):
    plural = ''
    if values > 1:
        plural = 's'

    return 'Error: %s takes %d value%s.' % (token, values, plural)


def rpn_calc(expr: str) -> float:
    stack = []

    for token in expr.split():
        if token in operators:
            try:
                if operators[token][1] == 1:
                    stack.append(operators[token][0](stack.pop()))
                elif operators[token][1] == 2:
                    stack.append(operators[token][0](stack.pop(-2), stack.pop()))
            except Exception:
                raise ValueError(error_string(token, operators[token][1]))
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError('Error: only real numbers or %s.' % ''.join(operators.keys()))

    return stack.pop()


if __name__ == '__main__':
    expression = input('# ')

    print(f"result={rpn_calc(expression)}")
