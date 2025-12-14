import operator

def calculate(a, op, b):
    """Performs arithmetic operations safely."""
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow
    }
    if op not in ops:
        raise ValueError("Invalid operator. Use +, -, *, /, %, or **.")
    if op == '/' and b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return ops[op](a, b)

# The rest of your calculator UI code would go here
# (the main() function we discussed earlier)