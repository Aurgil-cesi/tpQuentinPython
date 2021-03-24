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
    return "".join(list(map(lambda l: "*" if l.upper() not in letters else l, word)))

def run():
    print("=== Le pendu ===")
    word = words[random.randrange(0, len(words))]
    life = len(word)
    letters = list()
    
    hidden_word = hidden(word, letters)
    while life > 0 and word != hidden_word:

        print(f"Vies restantes : {life}")
        print(f"Mot à trouver : {hidden_word}")

        letter = input_char("Saisir une lettre : ").upper()
        letters.append(letter)
        hidden_word = hidden(word, letters)
        
        if letter.upper() not in word.upper():
            life -= 1

    print("Vous avez gagné" if word == hidden_word else "Vous avez perdu")

if __name__ == "__main__":
    run()