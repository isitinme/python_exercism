from functools import reduce

color_to_band = list([
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
])

OHMS = 'ohms'
KILO = 'kilo'
MEGA = 'mega'
GIGA = 'giga'
KILO_BITS = 3
MEGA_BITS = 6
GIGA_BITS = 9
NUM_OF_FIRST_BITS = 2
LAST_BIT_INDEX = 2

def is_kilo(n: int) -> bool:
    return n >= 10 ** 3 and n < 10 ** 6

def is_mega(n: int) -> bool:
    return n >= 10 ** 6 and n < 10 ** 9

def is_giga(n: int) -> bool:
    return n >= 10 ** 9

def label(colors):
    prefix_sum = str(
        # Prefix sum
        reduce(lambda x, y: int(
            str(color_to_band.index(x)) + str(color_to_band.index(y))
        ),
        colors[:NUM_OF_FIRST_BITS])
    )

    last_band_idx = color_to_band.index(colors[LAST_BIT_INDEX])
    zeros_from_last_band = '' if last_band_idx == 0 else ''.join([str(0) for _ in range(0, last_band_idx)])

    total_str = prefix_sum + zeros_from_last_band
    total_int = int(total_str)

    if is_giga(total_int):
        postfix = GIGA + OHMS
        prefix = total_str[:-GIGA_BITS]
    elif is_mega(total_int):
        postfix = MEGA + OHMS
        prefix = total_str[:-MEGA_BITS]
    elif is_kilo(total_int):
        postfix = KILO + OHMS
        prefix = total_str[:-KILO_BITS]
    else:
        prefix = total_str
        postfix = OHMS

    return '{} {}'.format(prefix, postfix)