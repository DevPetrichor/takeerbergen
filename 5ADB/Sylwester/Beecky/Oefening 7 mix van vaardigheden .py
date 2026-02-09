""" Oefening 7 mix van vaardigheden"""


print("Je hebt de keuze uit volgende selecties:")
print("Oefening 1: while-for loop.")
print("Oefening 2: Voorschot berekenen.")
print("Oefening 3: Gewicht omrekenen.")
oefening = int(input("Welke oefening kies je?")) # je invoer
if oefening == 1:
    # Opgave 1 herhaling for and while
    nummer = [1, 2, 3, 4, 5] # lijst met nummers
    i = 0
    while i < 2: # als i kleiner is dan 2
        for n in nummer: # als n 1 van de nummers is
            print(n)
        i += 1

elif oefening == 2:
    # Opgave 2 Voorschot berekenen
    print("Geef de prijs (euro) van de woning in?")
    prijs_Woning = float(input())
    print("Geef de waarde (euro) van je bankrekening in?")
    bankrekening = float(input())


    if bankrekening >= prijs_Woning * 0.25: # als bankrekening groter of gelijk is aan 25% van de prijs woning
        betalen_10 = prijs_Woning * 0.1
        print(f"Je moet 10% van het bedrag betalen, wat neerkomt op {betalen_10} euro.")

    elif bankrekening < prijs_Woning * 0.25: # als bankrekening kleiner is dan 25% van de prijs woning
        betalen_20 = prijs_Woning * 0.2
        print(f"Je moet 20% van het bedrag betalen, wat neerkomt op {betalen_20} euro.")

elif oefening == 3:
    # Opgave 3 Gewicht omrekenen
    print("Geef je gewicht in?")
    gewicht = float(input())
    print("Welke eenheid heb je gekozen? (Kg of Lbs)")
    eenheid = input()

    if eenheid == "Kg" or eenheid == "kg": # als eenheid kg is
        gewicht_Lbs = gewicht * 2.20462 # omrekenen naar lbs
        print(f"Je oorspronkelijk gewicht is {gewicht:.2f} kg en dit is omgezet {gewicht_Lbs:.2f} lbs.")

    elif eenheid == "Lbs" or eenheid == "lbs": # als eenheid lbs is
        gewicht_Kg = gewicht / 2.20462 # omrekenen naar kg
        print(f"Je oorspronkelijk gewicht is {gewicht:.2f} lbs en dit is omgezet {gewicht_Kg:.2f} kg.")

else:
    print("Ongeldige keuze, kies 1, 2 of 3.")