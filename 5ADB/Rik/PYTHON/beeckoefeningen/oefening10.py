def ElectrischeAuto():
    aankoopPrijs = 31895 #  whattherange.com/elektrische-auto - Volvo EX30
    onderhoud = 350 # Volvo Care Offer
    biv = 61.5 # belastingen.fenb.be - Simulatie
    verzekering = 1170 # verzekeringen.be - Yuzzu Full Omnium
    brandstof = 0.3306 # engie.be - Blog
    kwh = 51 # whattherange.com/elektrische-auto - Volvo EX30
    batterij = 254 # whattherange.com/elektrische-auto - Volvo EX30
    kilometers = 15000
    verkeersBelasting = 102.96 # belastingen.fenb.be - Simulatie
    totaalJaar = 17

    energiePerJaar = brandstof * kwh * (kilometers / batterij)

    totaalKM = kilometers * totaalJaar

    prijsEersteJaar = aankoopPrijs + onderhoud + biv + verzekering + energiePerJaar + verkeersBelasting
    prijsVervolgJaar = onderhoud + verzekering + energiePerJaar + verkeersBelasting

    for jaar in range(1, totaalJaar + 1):
        if jaar == 1:
            print(f"Jaar {jaar}: Prijs = {prijsEersteJaar:.2f}")
        else:
            uitgerekend = prijsVervolgJaar + prijsVervolgJaar * (jaar - 1)
            print(f"Jaar {jaar}: Prijs = {uitgerekend:.2f}")

    totaalPrijs = prijsEersteJaar + prijsVervolgJaar * (totaalJaar - 1)
    prijsPerKM = totaalPrijs / totaalKM

    print("De totale prijs van de auto over", totaalJaar, "jaar is:", f"{totaalPrijs:.2f}")
    print("De prijs per jaar is:", f"{totaalPrijs / totaalJaar:.2f}")
    print("De prijs per kilometer is:", f"{prijsPerKM:.2f}")
    print(f"Prijs eerste jaar: {prijsEersteJaar:.0f}")
    print(f"Prijs vervolgjaar: {prijsVervolgJaar:.0f}")

def BenzineAuto():
    aankoopPrijs = 31.499 # cardoen.be - Kia ProCeed
    onderhoud = 804 # cardoen.be - onderhoudscontract
    biv = 0 # belastingen.fenb.be - Simulatie
    verzekering = 1.248 # cardoen.be - autoverzekering
    brandstof = 1.861 # anwb.nl - Benzineprijs
    kilometers = 15000
    verkeersBelasting =   250.4 # belastingen.fenb.be - Simulatie
    totaalJaar = 17

    energiePerJaar = brandstof * (kilometers / 15) 

    totaalKM = kilometers * totaalJaar

    prijsEersteJaar = aankoopPrijs + onderhoud + biv + verzekering + energiePerJaar + verkeersBelasting
    prijsVervolgJaar = onderhoud + verzekering + energiePerJaar + verkeersBelasting

    for jaar in range(1, totaalJaar + 1):
        if jaar == 1:
            print(f"Jaar {jaar}: Prijs = {prijsEersteJaar:.2f}")
        else:
            uitgerekend = prijsVervolgJaar + prijsVervolgJaar * (jaar - 1)
            print(f"Jaar {jaar}: Prijs = {uitgerekend:.2f}")

    totaalPrijs = prijsEersteJaar + prijsVervolgJaar * (totaalJaar - 1)
    prijsPerKM = totaalPrijs / totaalKM

    print("De totale prijs van de auto over", totaalJaar, "jaar is:", f"{totaalPrijs:.2f}")
    print("De prijs per jaar is:", f"{totaalPrijs / totaalJaar:.2f}")
    print("De prijs per kilometer is:", f"{prijsPerKM:.2f}")
    print(f"Prijs eerste jaar: {prijsEersteJaar:.0f}")
    print(f"Prijs vervolgjaar: {prijsVervolgJaar:.0f}")

print("Elektrische Auto:")
ElectrischeAuto()
print("\nBenzine Auto:")
BenzineAuto()
