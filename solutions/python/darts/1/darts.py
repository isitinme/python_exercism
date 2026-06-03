import math

board_params = list([
    (1, 10),
    (5, 5),
    (10, 1),
    (11, 0)
])

def score(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    for param in board_params:
        range, value = param
        if distance <= range:
            return value
    return 0

print(
    score(-9, 9)
)