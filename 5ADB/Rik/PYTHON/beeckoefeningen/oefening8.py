fruit = {"appel": 2.5, "banaan": 1.80, "peer": 2.20} # prijzen per kg
keuze = str(input("Welk fruit wil je kopen? "))
if keuze in fruit: # controleer of het fruit in de lijst staat
    gewicht = float(input("Hoeveel kg wil je kopen? "))
    prijskg = fruit[keuze] # haal de prijs per kg op
    totaalprijs = gewicht * prijskg # bereken de totaalprijs
    if gewicht >= 5: # als het gewicht 5 kg of meer is
        korting = totaalprijs * 0.1 # pas 10% korting toe bij 5 kg of meer
    print(f"De totaalprijs voor {gewicht} kg {keuze} is {totaalprijs} euro.")
    if gewicht >= 5:
        print(f"Aangezien u {gewicht} kg {keuze} kocht, heeft u een korting van {korting} euro gekregen.")
        print(f"De te betalen prijs is {totaalprijs - korting} euro.")
else:
    print("Sorry, dat fruit hebben we niet.")


