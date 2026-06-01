class Auto:
    def __init__(self, merk, model, bouwjaar):
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar

    def __str__(self):
        return f"Merk: {self.merk}, Model: {self.model}, Bouwjaar: {self.bouwjaar}"


class Garage:
    def __init__(self):
        self.autos = []

    def auto_toevoegen(self, auto):
        self.autos.append(auto)
        print("De auto is succesvol toegevoegd aan de garage.")

    def autos_bekijken(self):
        if not self.autos:
            print("Er zijn geen auto's in de garage.")
        else:
            print("Auto's in de garage:")
            for idx, auto in enumerate(self.autos, start=1):
                print(f"{idx}. {auto}")

    def auto_verwijderen(self, index):
        if 0 <= index < len(self.autos):
            verwijderde_auto = self.autos.pop(index)
            print(f"De auto '{verwijderde_auto.merk} {verwijderde_auto.model}' is succesvol verwijderd.")
        else:
            print("Ongeldig nummer. Geen auto verwijderd.")


class GarageApp:
    def __init__(self):
        self.garage = Garage()

    def start(self):
        while True:
            print("\n--- Welkom bij de garage! ---")
            print("1: Auto binnenbrengen.")
            print("2: Auto bekijken.")
            print("3: Auto verwijderen.")
            print("4: Afsluiten.")
            
            try:
                keuze = int(input("Welke optie kies je? "))
            except ValueError:
                print("Ongeldige invoer.")
                continue

            if keuze == 1:
                self.auto_toevoegen_menu()

            elif keuze == 2:
                self.garage.autos_bekijken()

            elif keuze == 3:
                self.auto_verwijderen_menu()

            elif keuze == 4:
                print("Bedankt voor het bezoeken van de garage. Tot ziens!")
                break

            else:
                print("Ongeldige keuze.")

    def auto_toevoegen_menu(self):
        merk = input("Wat is het merk van de auto? ")
        model = input("Wat is het model van de auto? ")
        bouwjaar = int(input("Wat is het bouwjaar van de auto? "))
        auto = Auto(merk, model, bouwjaar)
        self.garage.auto_toevoegen(auto)

    def auto_verwijderen_menu(self):
        self.garage.autos_bekijken()
        if not self.garage.autos:
            return

        try:
            index = int(input("Welke auto wil je verwijderen? Kies een nummer: ")) - 1
            self.garage.auto_verwijderen(index)
        except ValueError:
            print("Ongeldige invoer. Geen auto verwijderd.")


# Programma starten
app = GarageApp()
app.start()