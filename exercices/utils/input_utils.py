import re

def input_number(texte):
    right = False
    entry = None
    while not right:
        entry = input(texte)
        try:
            entry = int(entry)
            right = True
        except:
            pass
    return entry

def input_number_range(texte, start, stop):
    right = False
    entry = None
    while not right:
        entry = input_number(texte)
        if entry in range(start, stop):
            right = True
    return entry

def input_positive(texte):
    right = False
    entry = None
    while not right:
        entry = input_number(texte)
        if entry > 0:
            right = True
    return entry

def input_char(texte):
    right = False
    entry = None
    while not right:
        entry = input(texte)
        if(re.search("^[a-zA-Z]$", entry)):
            right = True
    return entry