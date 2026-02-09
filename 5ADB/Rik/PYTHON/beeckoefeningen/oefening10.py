def ElectrischeAuto():
    aankoopPrijs = 50000
    onderhoud = 500
    biv = 64.5
    verzekering = 1200
    brandstof = 0.20   
    kwh = 70          
    batterij = 360   
    kilometers = 15000
    verkeersBelasting = 103
    totaalJaar = 17

    energiePerJaar = brandstof * kwh * (kilometers / batterij)

    totaalKM = kilometers * totaalJaar

    prijsEersteJaar = aankoopPrijs + onderhoud + biv + verzekering + energiePerJaar + verkeersBelasting
    prijsVervolgJaar = onderhoud + verzekering + energiePerJaar + verkeersBelasting

    for jaar in range(1, totaalJaar + 1):
        if jaar == 1:
            print(f"Jaar {jaar}: Prijs = {prijsEersteJaar:.2f}")
        else:
            print(f"Jaar {jaar}: Prijs = {prijsVervolgJaar:.2f} + {prijsVervolgJaar} * {jaar - 1}")

    totaalPrijs = prijsEersteJaar + prijsVervolgJaar * (totaalJaar - 1)
    prijsPerKM = totaalPrijs / totaalKM

    print("De totale prijs van de auto over", totaalJaar, "jaar is:", f"{totaalPrijs:.2f}")
    print("De prijs per jaar is:", f"{totaalPrijs / totaalJaar:.2f}")
    print("De prijs per kilometer is:", f"{prijsPerKM:.2f}")
    print(prijsEersteJaar)
    print(prijsVervolgJaar)

def BenzineAuto():
    aankoopPrijs = 40000
    onderhoud = 500
    biv = 500
    verzekering = 1200
    brandstof = 1.50   
    kilometers = 15000
    verkeersBelasting = 270
    totaalJaar = 17

    energiePerJaar = brandstof * (kilometers / 15) 

    totaalKM = kilometers * totaalJaar

    prijsEersteJaar = aankoopPrijs + onderhoud + biv + verzekering + energiePerJaar + verkeersBelasting
    prijsVervolgJaar = onderhoud + verzekering + energiePerJaar + verkeersBelasting

    for jaar in range(1, totaalJaar + 1):
        if jaar == 1:
            print(f"Jaar {jaar}: Prijs = {prijsEersteJaar:.2f}")
        else:
            prijsaa = prijsVprijsVervolgJaar * (jaar - 1)
            print(f"Jaar {jaar}: Prijs = {prijsVervolgJaar:.2f} + {prijsVervolgJaar} * {jaar - 1}")

    totaalPrijs = prijsEersteJaar + prijsVervolgJaar * (totaalJaar - 1)
    prijsPerKM = totaalPrijs / totaalKM

    print("De totale prijs van de auto over", totaalJaar, "jaar is:", f"{totaalPrijs:.2f}")
    print("De prijs per jaar is:", f"{totaalPrijs / totaalJaar:.2f}")
    print("De prijs per kilometer is:", f"{prijsPerKM:.2f}")
    print(prijsEersteJaar)
    print(prijsVervolgJaar)

print("Elektrische Auto:")
ElectrischeAuto()
print("\nBenzine Auto:")
BenzineAuto()
