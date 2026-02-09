"""Opgave 8 Garage"""

Garage = []  # lege lijst voor auto's

while True: # oneindige loop voor het menu
    print("--- Welkom bij de garage! ---")
    print("Kies een van de volgende opties:")
    print("1: Auto binnenbrengen.")
    print("2: Auto bekijken.")
    print("3: Auto verwijderen.")
    print("4: Afsluiten.")
    keuze = int(input("Welke optie kies je? "))
    if keuze == 1: # auto toevoegen
        merk = input("Wat is het merk van de auto? ")
        model = input("Wat is het model van de auto? ")
        bouwjaar = int(input("Wat is het bouwjaar van de auto? "))
        auto = {"merk": merk, "model": model, "bouwjaar": bouwjaar} # auto als dictionary
        Garage.append(auto) # auto toevoegen aan de lijst
        print("De auto is succesvol toegevoegd aan de garage.")

    elif keuze == 2: # auto's bekijken
        if len(Garage) == 0:
            print("Er zijn geen auto's in de garage.")
        else:
            print("Auto's in de garage:")
            for idx, auto in enumerate(Garage, start=1):
                print(f"{idx}. Merk: {auto['merk']}, Model: {auto['model']}, Bouwjaar: {auto['bouwjaar']}") # auto's weergeven met nummer

    elif keuze == 3: # auto verwijderen
        if len(Garage) == 0:
            print("Er zijn geen auto's in de garage om te verwijderen.")
        else:
            print("Auto's in de garage:")
            for idx, auto in enumerate(Garage, start=1):
                print(f"{idx}. Merk: {auto['merk']}, Model: {auto['model']}, Bouwjaar: {auto['bouwjaar']}") # auto's weergeven met nummer
            try: # verwijderen uit de lijst met foutafhandeling
                verwijder_index = int(input("Welke auto wil je verwijderen? Kies een nummer: ")) - 1
                if 0 <= verwijder_index < len(Garage):
                    verwijderde_auto = Garage.pop(verwijder_index)
                    print(f"De auto '{verwijderde_auto['merk']} {verwijderde_auto['model']}' is succesvol verwijderd.")
                else:
                    print("Ongeldig nummer. Geen auto verwijderd.")
            except ValueError: # foutafhandeling voor niet-integer invoer
                print("Ongeldige invoer. Geen auto verwijderd.")

    elif keuze == 4:
        print("Bedankt voor het bezoeken van de garage. Tot ziens!")
        break 