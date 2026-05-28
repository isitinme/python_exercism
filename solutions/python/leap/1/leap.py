FOUR = 4
HUNDRED = 100
FOUR_HUNDRED = 400

def is_evenly_divisible(num, division):
    return num % division == 0

def leap_year(year):
    return True if is_evenly_divisible(year, FOUR) and not is_evenly_divisible(year, HUNDRED) else is_evenly_divisible(year, FOUR_HUNDRED)