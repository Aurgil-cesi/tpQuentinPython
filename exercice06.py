import math

def factorial(number):


    # Recursive
    # facto = 1 if abs(number) == 1 else (abs(number) * factorial(abs(number) - 1))
    # return facto if number >= 0 else facto * -1

    # Une ligne
    return math.factorial(abs(number)) if number >= 0 else math.factorial(abs(number)) * -1

def run():
    for test in [(1, 1), (2, 2), (3, 6), (4, 24), (8, 40320), (-8, -40320)]:
        assert factorial(test[0]) == test[1]