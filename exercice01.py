a, b = 1, 2
a, b = b, a

def run():
    for test in [(a, 2), (b, 1)]:
        assert test[0] == test[1]