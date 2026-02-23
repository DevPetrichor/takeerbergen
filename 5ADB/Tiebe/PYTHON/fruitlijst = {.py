fruitlijst = {# dit is de fruitlijst
    "appel": 2.5,
    "banaan": 1.80,
    "peer": 2.20,
}
fruit = input("Welke fruitsoort wil je kopen? ") #dit vraagt welke fruitsoort je wilt kopen
    
if fruit in fruitlijst:#als de fruitsoort in de lijst staat gaat dit door
        aantal = int(input("Hoeveel kg wil je kopen? "))#berekent de prijs
        if aantal >= 5: #korting voor aankopen vanaf de 5 kg
            kortingsprijs = float(fruitlijst[fruit]) * 0.9 #10% korting

        prijs = float(fruitlijst[fruit])
        totaal_prijs = prijs* aantal
        print(f"De totale prijs voor {aantal} kg {fruit} is €{totaal_prijs:.2f}")#dit toont de totale prijs
        if aantal >= 5: #korting voor aankopen vanaf de 5 kg
            print(f"Door de korting van {kortingsprijs:.2f} is €{totaal_prijs - kortingsprijs:.2f}")#dit toont de totale prijs met korting
else:#als de fruitsoort niet in de lijst staat gaat dit door
        print("niet beschikbaar")
        