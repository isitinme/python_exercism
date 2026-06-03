"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    cap_letters = list(range(65, 69))
    i = 0
    j = 0
    while i < number:
        if j == 4:
            j = 0
        yield chr(cap_letters[j])
        i += 1
        j += 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    cap_letters = list(range(65, 69))
    i = 0
    j = 0
    row = 1
    while i < number:
        if j == 4:
            row += 1
            if row == 13:
                continue
            j = 0
        
        letter = chr(cap_letters[j])
        yield str(row) + letter
        i += 1
        j += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    res = dict()
    gen = generate_seats(len(passengers))
    for item in passengers:
        res[item] = next(gen)
    return res


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    code_len = 12
    for seat in seat_numbers:
        remain_space = code_len - len(seat + flight_id)
        if remain_space > 0:
            postfix = [str(0) for _ in range(0, remain_space)]
        yield seat + flight_id + ''.join(postfix)

g = generate_seats(
    14 * 4
)
for i in g:
    print(i)