def get_category(age):
    if(age < 6):
        raise ValueError()
    else:
        return "Poussin" if age < 8 else "Pupille" if age < 10 else "Minime" if age < 12 else "Cadet"

def run():
    for test in [("Poussin", (6, 7)), ("Pupille", (8, 9)), ("Minime", (10, 11)), ("Cadet", (12, 99))]:
        for num in test[1]:
            assert get_category(num) == test[0]

    try:
        get_category(1)
        raise AssertionError()
    except ValueError:
        pass
