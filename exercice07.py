import re

def get_letter_count(word):
    return len(re.findall("[a-zA-Z]", word))
    # return len(list(filter(lambda i: i.isalpha(), [l for l in word])))

def run():
    for test in [("Oui", 3), ("Bonjour", 7), ("", 0), (".........hein???", 4), ("Attention y'a quatre mots !", 21)]:
        assert get_letter_count(test[0]) == test[1]