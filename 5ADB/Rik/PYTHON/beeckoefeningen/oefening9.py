def oefening1():
    nummers = [1, 2, 3, 4, 5]
    for nummer in nummers:
        print(nummer)
    i = 0
    while i < len(nummers):
        print(nummers[i])
        i += 1


def oefening2():
    woning = int(input("Geef de prijs (euro)  van de woning in: "))
    rekening = int(input("Geef de waarde (euro) van je bankrekening in: "))
    if woning*0.25 <= rekening:
        if rekening >= woning:
            voorschot = 0.10
            print(f"Je moet een voorschot betalen van {voorschot * woning} euro.")
        else:
            voorschot = 0.20
            print(f"Je moet een voorschot betalen van {voorschot * woning} euro.")
    else:
        print("Je hebt niet genoeg geld op je rekening voor een voorschot.")

def oefening3():
    gewicht = int(input("Geef je gewicht in: "))
    eenheid = input("Welke eenheid heb je gekozen? (kg/lb): ").lower()
    if eenheid == "kg" or eenheid == "lb":
        if eenheid == "kg":
            omgezet_gewicht = gewicht * 2.20462
            print(f"Je oorspongelijk gewicht was {gewicht} kg en dit is omgezet {omgezet_gewicht:.2f} lbs")
        else:
            omgezet_gewicht = gewicht / 2.20462
            print(f"Je oorspongelijk gewicht was {gewicht} lbs en dit is omgezet {omgezet_gewicht:.2f} kg")
    else:
        print("Ongeldige eenheid gekozen.")

optie = int(input("Je hebt de keuze uit volgende selecties:\nOefening 1: while-for loop.\nOefening 2: Voorschot berekenen.\nOefening 3: Gewicht omzetten.\n\nWelke oefening kies je? "))
if optie > 3 or optie < 1:
    print("Ongeldige keuze, programma wordt afgesloten.")
else:
    if optie == 1:
        oefening1()
    elif optie == 2:
        oefening2()
    else:
        oefening3()


