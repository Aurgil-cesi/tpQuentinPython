import random

def roulette(numero, somme):
    gagnant = random.randrange(0, 50)

    return (gagnant, somme * 3 if gagnant == numero else somme * 0.5 if gagnant % 2 == numero % 2 else 0)

numero, somme = -1, -1
while not int(numero) in range(1, 51):
    numero = input("Votre numéro (1 - 50) : ")
numero = int(numero)
somme = int(input("La somme misée : "))

resultat = roulette(numero, somme)

print("=== La roulette ===")
print(f"Le numéro misé est : {numero}")
print(f"La somme misée est : {somme}")
print(f"Le numéro gagnant est : {resultat[0]}")
print(f"La somme gagnée est : {resultat[1]}")