def oefening1():
    nummers = [1, 2, 3, 4, 5]
    for nummer in nummers:
        print(nummer)
    i = 0
    while i < len(nummers):
        print(nummers[i])
        i += 1


def oefening2():
    pass

def oefening3():
    pass

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