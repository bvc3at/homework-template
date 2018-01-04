from functools import reduce


def modulo_five():
    return list(map(lambda x: x % 5, [1, 4, 5, 30]))


def to_string():
    return list(map(lambda x: str(x), [3, 4, 90, -2]))


def filter_string():
    return list(filter(lambda x: not isinstance(x, str), ['some', 1, 'v', 40, '3a', str]))


def count_letters():
    def reducer(left, right):
        left_count = len(left) if isinstance(left, str) else left
        return left_count + len(right)
    return reduce(reducer, ['some', 'other', 'value'])
