# vergelijken wat de uitgaven en uitstoten tussen een elektrische auto (willekeurig) en benzine (willekeurig)
# Rekening houden met de aanschafprijs, onderhoudskosten, brandstofkosten en uitstoot van beide auto's
# Tis belangerijk als je in de toekomst een auto wilt kopen, en je wilt weten welke beter is voor jou en het milieu
# Elektrische auto: Tesla Model 3 preformance
# Benzine auto: Ford Mustang GT
# Bronnen:
# https://www.tesla.com/nl_be/model3
# https://www.nl.ford.be/alle-modellen/new-mustang#models
# AI overzicht van Google
"""
Aanschafprijs_tesla = 58490 # prijs van een nieuwe Tesla Model 3
Aanschafprijs_ford = 58960 # prijs van een nieuwe Ford Mustang GT
Onderhoudskosten_tesla = 500 
Onderhoudskosten_ford = 500
BIV_tesla = 61.50
BIV_ford = 1000 # Belasting op Inverkeerstelling, eenmalige belasting bij aanschaf van een auto in België
verkeersbelasting_tesla = 150 # jaarlijkse verkeersbelasting voor een Tesla Model 3
Verzekering_tesla = 1200 # jaarlijkse verzekering voor een Tesla Model 3
Verkeersbelasting_ford = 400 # jaarlijkse verkeersbelasting voor een Ford Mustang GT
Verzekering_ford = 800 # jaarlijkse verzekering voor een Ford Mustang GT
Brandstofkosten_tesla = 0.20 # KWh prijs
Brandstofkosten_ford = 2.20 # per liter benzine
Verbruik_tesla = 15 / 100 # 15 KWh per 100 km
Verbruik_ford = 12 / 100 # 12 liter per 100 km
maximale_leeftijd_tesla = 260000 # maximale leeftijd van een Tesla Model 3
maximale_leeftijd_ford = 350000 # maximale leeftijd van een Ford Mustang GT
afstand_lege_tank_tesla = 513 # afstand in km die een Tesla Model 3 kan rijden na een volledige batterij
afstand_lege_tank_ford = 508 # afstand in km die een Ford Mustang GT kan rijden na een volledige tank benzine
Uitstoot_tesla = 0 # elektrische auto's stoten geen CO2 uit tijdens het rijden
Uitstoot_productie_tesla = 20000 # gram CO2 per auto geproduceerd
Uitstoot_ford = 280 # gram CO2 per kilometer
Uitstoot_productie_ford = 5000 # gram CO2 per auto geproduceerd
Afstand_per_jaar = 15000 # gemiddelde afstand die een auto per jaar rijdt


brandstofkosten_per_jaar_tesla = Afstand_per_jaar * Verbruik_tesla * Brandstofkosten_tesla # aantal keer dat de Tesla volledig opgeladen moet worden per jaar
brandstofkosten_per_jaar_ford = Afstand_per_jaar * Verbruik_ford * Brandstofkosten_ford # aantal keer dat de Ford volledig getankt moet worden per jaar
Totale_kosten_tesla = Aanschafprijs_tesla + BIV_tesla + Onderhoudskosten_tesla * maximale_leeftijd_tesla / Afstand_per_jaar + Verzekering_tesla * maximale_leeftijd_tesla / Afstand_per_jaar + brandstofkosten_per_jaar_tesla
Totale_kosten_ford = Aanschafprijs_ford + BIV_ford + Onderhoudskosten_ford * maximale_leeftijd_ford / Afstand_per_jaar + Verzekering_ford * maximale_leeftijd_ford / Afstand_per_jaar + brandstofkosten_per_jaar_ford
Jaren_rijden_tesla = maximale_leeftijd_tesla / Afstand_per_jaar
Jaren_rijden_ford = maximale_leeftijd_ford / Afstand_per_jaar
print(f"Totale kosten over de levensduur van de Tesla Model 3: €{round(Totale_kosten_tesla, 2)} met het levensduur van {maximale_leeftijd_tesla} km in {Jaren_rijden_tesla} jaar")
print(f"Totale kosten over de levensduur van de Ford Mustang GT: €{round(Totale_kosten_ford, 2)} met het levensduur van {maximale_leeftijd_ford} km in {Jaren_rijden_ford} jaar")
jaar_rijden = int(input("Hoeveel jaar wil je de auto rijden? "))

jaarlijkse_kosten_tesla = Onderhoudskosten_tesla + Verzekering_tesla + brandstofkosten_per_jaar_tesla + verkeersbelasting_tesla
jaarlijkse_kosten_ford = Onderhoudskosten_ford + Verzekering_ford + brandstofkosten_per_jaar_ford + Verkeersbelasting_ford

totale_uitstoot_tesla = Uitstoot_productie_tesla
totale_uitstoot_ford = Uitstoot_productie_ford + Uitstoot_ford * Afstand_per_jaar * jaar_rijden


print(f"De vergelijking in {jaar_rijden} jaar is: ")
print(f"Totale kosten over {jaar_rijden} jaar voor de Tesla Model 3: €{round(jaarlijkse_kosten_tesla * jaar_rijden, 2)}")
print(f"Totale kosten over {jaar_rijden} jaar voor de Ford Mustang GT: €{round(jaarlijkse_kosten_ford * jaar_rijden, 2)}")
print(f"Gemiddelde jaarlijkse kosten voor de Tesla Model 3: €{round(jaarlijkse_kosten_tesla, 2)}")
print(f"Gemiddelde jaarlijkse kosten voor de Ford Mustang GT: €{round(jaarlijkse_kosten_ford, 2)}")
print(f"Je Tesla Model 3 produceert geen CO2 dus je hebt aleen de productie van: {round(totale_uitstoot_tesla / 1000, 2)} kilogram CO2")
print(f"Totale uitstoot over {jaar_rijden} jaar voor de Ford Mustang GT: {round(totale_uitstoot_ford / 1000, 2)} kilogram CO2")

vershill_kosten_jaarlijks = jaarlijkse_kosten_ford - jaarlijkse_kosten_tesla

print(f"Verschil in jaarlijkse kosten tussen de Ford Mustang GT en de Tesla Model 3: €{round(vershill_kosten_jaarlijks, 2)}")
"""

class TeslaModel3:
    def __init__(self):
        self.aanschafprijs = 58490
        self.onderhoudskosten = 500
        self.biv = 61.50
        self.verkeersbelasting = 150
        self.verzekering = 1200
        self.brandstofkosten = 0.20
        self.verbruik = 15 / 100
        self.maximale_leeftijd = 260000
        self.afstand_lege_tank = 513
        self.uitstoot = 0
        self.uitstoot_productie = 20000
    def totale_uitstoot(self, afstand_per_jaar, jaar_rijden):
        return self.uitstoot_productie + self.uitstoot * afstand_per_jaar * jaar_rijden

class FordMustangGT:
    def __init__(self):
        self.aanschafprijs = 58960
        self.onderhoudskosten = 500
        self.biv = 1000
        self.verkeersbelasting = 400
        self.verzekering = 800
        self.brandstofkosten = 2.20
        self.verbruik = 12 / 100
        self.maximale_leeftijd = 350000
        self.afstand_lege_tank = 508
        self.uitstoot = 280
        self.uitstoot_productie = 5000
    def totale_uitstoot(self, afstand_per_jaar, jaar_rijden):
        return self.uitstoot_productie + self.uitstoot * afstand_per_jaar * jaar_rijden
    
afstand_per_jaar = 15000
jaar_rijden = int(input("Hoeveel jaar wil je de auto rijden? "))
print(f"Hier is de vergelijking tussen de Tesla Model 3 en de Ford Mustang GT na {jaar_rijden} jaar:")
print(f"De totale uitstoot is {FordMustangGT.totale_uitstoot} ")


