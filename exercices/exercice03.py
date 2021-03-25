def is_product_negative(a, b):
    return True if (a < 0 or b < 0) and not (a < 0 and b < 0) else False

def run():
    for test in [((6, 7), False), ((1, 0), False), ((-1, 5), True), ((1, -5), True), ((-1, -5), False)]:
        assert is_product_negative(test[0][0], test[0][1]) == test[1]
