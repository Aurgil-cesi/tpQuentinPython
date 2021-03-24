def square(number):
    return number * number

def run():
    for test in [(1, 1), (2, 4), (3, 9), (23, 529), (-23, 529)]:
        assert square(test[0]) == test[1]
