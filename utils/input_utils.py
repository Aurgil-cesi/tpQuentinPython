import re

def inputNumber(texte):
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

def inputNumberRange(texte, start, stop):
    right = False
    entry = None
    while not right:
        entry = inputNumber(texte)
        if entry in range(start, stop):
            right = True
    return entry

def inputPositive(texte):
    right = False
    entry = None
    while not right:
        entry = inputNumber(texte)
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