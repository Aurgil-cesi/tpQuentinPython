import re

def get_word_count(sentence):
    return len(re.findall("[a-zA-Z]+", sentence))
    # return len(list(filter(lambda i: i.isalpha(), [word for word in sentence.split(" ")])))

def run():
    for test in [("Bonjour", 1), ("Bonjour toi", 2), ("Bonjour ca va ?", 3), ("Bonjour ca va toi ?!", 4), ("", 0)]:
        assert get_word_count(test[0]) == test[1]
