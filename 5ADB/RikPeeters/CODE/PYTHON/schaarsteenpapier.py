import random

wins = 0
loses = 0
gelijk = 0

opties = ["schaar", "steen", "papier"]

while True:
    user = input("Kies Schaar, Steen of Papier (typ 'stop' om te stoppen): ").lower()
    if user == "stop":
        print("Spel gestopt!")
        print(f"Eindstand: Gewonnen: {wins}, Verloren: {loses}, Gelijk: {gelijk}")
        break

    optie = random.choice(opties)

    if user in opties:
        print(f"Jou optie: {user}\nMijn optie: {optie}")
        
        if user == optie:
            print("Gelijkspel!")
            gelijk += 1

        elif (user == "schaar" and optie == "papier") or \
             (user == "steen" and optie == "schaar") or \
             (user == "papier" and optie == "steen"):
            print("Je wint!")
            wins += 1
        
        else:
            print("Je bent verloren.")
            loses += 1

    else:
        print("Ongeldige keuze! Kies schaar, steen of papier.")
