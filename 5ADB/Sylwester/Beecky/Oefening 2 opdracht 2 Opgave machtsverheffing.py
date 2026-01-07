getal = int(input("Geef het getal waarvan je de kwadraat wilt berekenen:\n")) # Vraag een geheel getal aan de gebruiker
berekeningresultaat = getal ** 2 # Bereken het kwadraat van het getal
print("Het berekent getal is: ",berekeningresultaat) # Print het resultaat in een duidelijke zin
print("Wil je het resultaat handmatig controleren? (Y/N) ") # Vraag de gebruiker of hij het resultaat handmatig wil controleren
antwoord = input() # Lees het antwoord van de gebruiker

if antwoord.lower() == 'y': # Als het antwoord 'Y' is (ja)
    print(f"Handmatig berekenen: {getal} x {getal} =", getal*getal) # Print de handmatige berekening
    if getal*getal == berekeningresultaat: # Controleer of het handmatige resultaat gelijk is aan het berekende resultaat
        print("Het resultaat is correct!")          