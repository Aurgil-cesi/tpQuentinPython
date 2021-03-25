exercises = list(map(__import__, [f"exercice0{num}" for num in range(1, 9)]))

for i in range(len(exercises)):
    try:
        exercises[i].run()
        print(f"✅ Exercice {i + 1} : passé")
    except AssertionError:
        print(f"❌ Exercice {i + 1} : raté")
