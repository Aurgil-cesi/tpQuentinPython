import random
from utils.input_utils import input_char

words = [
    "Python",
    "Est",
    "Un",
    "Excelent",
    "Langage",
    "De",
    "Programmation"
]

def hidden(word, letters):
    trans = ""
    for l in word:
        if l.upper() not in letters:
            trans = trans + "*"
        else:
            trans = trans + l
    return trans

def run():
    word = words[random.randrange(0, len(words))]
    life = len(word)

    letters = list()
    myWord = hidden(word, letters)
    print("=== Le pendu ===")
    while life > 0 and word != myWord:
        print(f"Vies restantes : {life}")
        print(f"Mot à trouver : {myWord}")
        letter = input_char("Saisir une lettre : ")
        letters.append(letter.upper())
        myWord = hidden(word, letters)

        if letter.upper() not in word.upper():
            life -= 1

    if(word == myWord):
        print("Vous avez gagné")
    else:
        print("Vous avez perdu")

if __name__ == "__main__":
    run()