lijst = {
    "appel": "1",
    "banaan": "1.2",
    "kers": "0.8",
    "druif": "1.4",
    "mango": "1.6",
    "peer": "1",
    "sinaasappel": "0.95",
    "watermeloen": "1.3"
}

while True:
    fruit = input("Welke fruitsoort wil je kopen? ").lower()
    
    if fruit in lijst:
        aantal = int(input("Hoeveel kg wil je kopen? "))
        prijs_per_kg = float(lijst[fruit])
        totaal_prijs = prijs_per_kg * aantal
        print(f"De totale prijs voor {aantal} kg {fruit} is €{totaal_prijs:.2f}")
     
    else:
        print("Sorry, deze fruitsoort is niet beschikbaar.")
        