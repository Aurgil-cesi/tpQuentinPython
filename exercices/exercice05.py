def is_number_correct(number):
    return 10 <= number <= 20, 10 - number if number < 10 else 20 - number if number > 20 else 0

def run():
    for test in [(0, (False, 10)), (10, (True, 0)), (20, (True, 0)), (21, (False, -1)), (50, (False, -30)), (15, (True, 0))]:
        assert is_number_correct(test[0]) == test[1]
