resistor_bands = list([
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

def color_code(color):
    return resistor_bands.index(color)

def colors():
    return resistor_bands