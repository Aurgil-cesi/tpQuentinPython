import random
from utils.input_utils import input_number_range, input_positive

def roulette(numero, somme):
    gagnant = random.randrange(0, 50)

    return (gagnant, somme * 3 if gagnant == numero else somme * 0.5 if gagnant % 2 == numero % 2 else 0)

def run():
    numero = input_number_range("Votre numéro (1 - 50) : ", 1, 51)
    somme = input_positive("La somme misée : ")

    resultat = roulette(numero, somme)

    print("=== La roulette ===")
    print(f"Le numéro misé est : {numero}")
    print(f"La somme misée est : {somme}")
    print(f"Le numéro gagnant est : {resultat[0]}")
    print(f"La somme gagnée est : {resultat[1]}")

if __name__ == "__main__":
    run()