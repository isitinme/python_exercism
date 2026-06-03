MIN_SQUARE = 1
MAX_SQUARE = 64

def square(number):
    if number < MIN_SQUARE or number > MAX_SQUARE:
        raise ValueError(f'square must be between {MIN_SQUARE} and {MAX_SQUARE}')
    if number == 1:
        return 1
    return square(number - 1) * 2

def total():
    i = MAX_SQUARE
    res = 0
    while i > 0:
        res = sum([res, square(i)])
        i -= 1
    return res