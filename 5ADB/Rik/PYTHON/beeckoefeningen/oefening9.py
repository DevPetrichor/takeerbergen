def oefening1():
    nummers = [1, 2, 3, 4, 5] #lijst met nummers
    for nummer in nummers:
        print(nummer)
    i = 0
    while i < len(nummers): #lengte van de lijst
        print(nummers[i]) #toont elk nummer in de lijst
        i += 1


def oefening2():
    woning = int(input("Geef de prijs (euro)  van de woning in: ")) #prijs woning
    rekening = int(input("Geef de waarde (euro) van je bankrekening in: "))
    if woning*0.25 <= rekening: #25% van de woningprijs
        if rekening >= woning:
            voorschot = 0.10 #10% voorschot
            print(f"Je moet een voorschot betalen van {voorschot * woning} euro.")
        else:
            voorschot = 0.20 #20% voorschot
            print(f"Je moet een voorschot betalen van {voorschot * woning} euro.")
    else:
        print("Je hebt niet genoeg geld op je rekening voor een voorschot.")

def oefening3():
    gewicht = int(input("Geef je gewicht in: ")) #gewicht invoeren
    eenheid = input("Welke eenheid heb je gekozen? (kg/lb): ").lower() #eenheid invoeren
    if eenheid == "kg" or eenheid == "lb":
        if eenheid == "kg":
            omgezet_gewicht = gewicht * 2.20462 #omzetten naar lbs
            print(f"Je oorspongelijk gewicht was {gewicht} kg en dit is omgezet {omgezet_gewicht:.2f} lbs") #:.2f voor 2 decimalen
        else:
            omgezet_gewicht = gewicht / 2.20462 #omzetten naar kg
            print(f"Je oorspongelijk gewicht was {gewicht} lbs en dit is omgezet {omgezet_gewicht:.2f} kg") #:.2f voor 2 decimalen
    else:
        print("Ongeldige eenheid gekozen.")

optie = int(input("Je hebt de keuze uit volgende selecties:\nOefening 1: while-for loop.\nOefening 2: Voorschot berekenen.\nOefening 3: Gewicht omzetten.\n\nWelke oefening kies je? "))
if optie > 3 or optie < 1: #controle geldige keuze
    print("Ongeldige keuze, programma wordt afgesloten.") 
else:
    if optie == 1:
        oefening1() #uitvoeren oefening 1
    elif optie == 2:
        oefening2() #uitvoeren oefening 2
    else:
        oefening3() #uitvoeren oefening 3


