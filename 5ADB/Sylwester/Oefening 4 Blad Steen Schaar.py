import random

opties = ["steen", "papier", "schaar"] # Definieer de mogelijke opties

while True:
    computer_keuze = random.choice(opties) # Laat de computer een willekeurige keuze maken
    speler_keuze = input("Kies steen, papier of schaar: ").lower() # Vraag de speler om een keuze te maken

    print(f"De computer koos: {computer_keuze}") # Print de keuze van de computer

    if speler_keuze == computer_keuze: # Controleer of het gelijkspel is
        print("Gelijkspel!")
    elif (speler_keuze == "steen" and computer_keuze == "schaar") or \
         (speler_keuze == "papier" and computer_keuze == "steen") or \
         (speler_keuze == "schaar" and computer_keuze == "papier"):
        print("Jij wint!")
    else:
        print("De computer wint!")
    
    opnieuw = input("Wil je nog een keer spelen? (ja/nee): ").lower() # Vraag of de speler opnieuw wil spelen
    if opnieuw != "ja":
        break # Stop het spel als de speler niet opnieuw wil spelen
print("Bedankt voor het spelen!")