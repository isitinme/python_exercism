"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time by the number of lasagna layers

    :param number_of_layers: int - number of layers lasagna should have
    :return: int - number of minutes to prepare this lasagna
    """
    return PREPARATION_TIME * number_of_layers
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time in minutes a lasagna has been cooking

    :param number_of_layers: int - number of layers lasagna should have
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - number of minutes a lasagna has been cooking

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
