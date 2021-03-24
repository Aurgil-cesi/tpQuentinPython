import random

words = [
    "Python",
    "Est",
    "Un",
    "Excelent",
    "Langage",
    "De",
    "Programmation"
]

def inWord(word, letter):
    return True if letter.upper() in word.upper() else False

def getWord(words):
    return words[random.randrange(0, len(words))]

def transforme(word, letters):
    trans = ""
    for l in word:
        if l.upper() not in letters:
            trans = trans + "*"
        else:
            trans = trans + l
    return trans

word = getWord(words)
life = len(word)

letters = list()
myWord = transforme(word, letters)
print("=== Le pendu ===")
while life > 0 and word != myWord:
    print(f"Vie restant : {life}")
    print(f"Mot à trouver : {myWord}")
    letter = input("Saisir une lettre : ")
    letters.append(letter.upper())
    myWord = transforme(word, letters)

    if(not inWord(word, letter)):
        life -= 1

if(word == myWord):
    print("Vous avez gagné")
else:
    print("Vous avez perdu")