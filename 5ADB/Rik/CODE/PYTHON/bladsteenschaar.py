opties = ["schaar", "steen", "papier"]

speler1 = input("Kies een optie: ").lower()
speler2 = input("Kies een optie: ").lower()

if speler1 not in opties or speler2 not in opties:
    print("Ongeldig optie, kies uit:", opties)

else:
    if (speler1 == "schaar" and speler2 == "papier") or \
             (speler1 == "steen" and speler2 == "schaar") or \
             (speler1 == "papier" and speler2 == "steen"):
        print("Speler 1 wint")
    elif speler1 == speler2:
        print("Gelijk spel!")
    else:
        print("Speler 2 wint")
