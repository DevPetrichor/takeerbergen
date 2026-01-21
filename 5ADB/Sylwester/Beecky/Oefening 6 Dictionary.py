fruiten = { # je dictionary met fruit en hun prijzen per kg
    "appel": 2.5,
    "banaan": 1.8,
    "peer": 2.2,
}
fruit = input("Welke fruit wil je kopen? ") #vraag de gebruiker om een fruitsoort

if fruit in fruiten: #controleer of de fruitsoort in de dictionary staat
    prijs = fruiten[fruit]
    aantal = int(input(f"Hoeveel kg {fruit} wil je kopen? "))
    if aantal >= 5: #korting voor aankopen vanaf de 5 kg
        prijs *= 0.9 #10% korting
    totaal = prijs * aantal
    print(f"De prijs per kg is €{prijs:.2f}.") #toon de prijs per kg
    print(f"De totale prijs voor {aantal} kg {fruit}(s) zonder korting is €{totaal / 0.9:.2f}.") #toon de totale prijs zonder korting
    print(f'De korting vanaf 5 kg is 10%.') #toon de korting
    print(f"De totale prijs voor {aantal} kg {fruit}(s) is €{totaal:.2f}. met korting") #toon de totale prijs met korting


else: #fruit is niet in de dictionary
    print(f"Sorry, we hebben die fruit niet in ons assortiment.")
