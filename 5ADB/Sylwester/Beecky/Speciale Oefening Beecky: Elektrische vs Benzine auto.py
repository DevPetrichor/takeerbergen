# vergelijken wat de uitgaven en uitstoten tussen een elektrische auto (willekeurig) en benzine (willekeurig)
# Rekening houden met de aanschafprijs, onderhoudskosten, brandstofkosten en uitstoot van beide auto's
# Tis belangerijk als je in de toekomst een auto wilt kopen, en je wilt weten welke beter is voor jou en het milieu
# Elektrische auto: Tesla Model 3 preformance
# Benzine auto: Ford Mustang GT
# Bronnen:
# https://www.tesla.com/nl_be/model3
# https://www.nl.ford.be/alle-modellen/new-mustang#models
# AI overzicht van Google
class Auto:
    def __init__(self, naam: str = 'Onbekend', aanschafprijs: float = 0, onderhoudskosten: float = 0, biv: float = 0, verkeersbelasting: float = 0,
                 verzekering: float = 0, brandstofkosten: float = 0, verbruik: float = 0, maximale_leeftijd: int = 0,
                 afstand_lege_tank: int = 0, uitstoot: int = 0, uitstoot_productie: int = 0):

        self.naam = naam
        self.aanschafprijs = aanschafprijs
        self.onderhoudskosten = onderhoudskosten
        self.biv = biv
        self.verkeersbelasting = verkeersbelasting
        self.verzekering = verzekering
        self.brandstofkosten = brandstofkosten
        self.verbruik = verbruik
        self.maximale_leeftijd = maximale_leeftijd
        self.afstand_lege_tank = afstand_lege_tank
        self.uitstoot = uitstoot
        self.uitstoot_productie = uitstoot_productie

    def totale_uitstoot(self, afstand_per_jaar, jaar_rijden):
        return self.uitstoot_productie + self.uitstoot * afstand_per_jaar * jaar_rijden

    def kosten_per_km(self, afstand_per_jaar):
        afschrijving_per_km = self.aanschafprijs / self.maximale_leeftijd
        brandstof_kosten_per_km = self.verbruik * self.brandstofkosten
        vaste_kosten_per_km = (self.onderhoudskosten + self.biv +
                               self.verkeersbelasting + self.verzekering) / afstand_per_jaar
        return afschrijving_per_km + brandstof_kosten_per_km + vaste_kosten_per_km

    def totale_kosten(self, afstand_per_jaar, jaar_rijden):
        afschrijving = self.aanschafprijs * (afstand_per_jaar * jaar_rijden / self.maximale_leeftijd)
        brandstof = self.brandstofkosten * self.verbruik * afstand_per_jaar * jaar_rijden
        vaste_kosten = (self.onderhoudskosten + self.biv +
                        self.verkeersbelasting + self.verzekering) * jaar_rijden
        return afschrijving + brandstof + vaste_kosten

Auto_Elektrisch = Auto(
    naam = input("Wat is de naam van de elektrische auto? "),
    aanschafprijs = float(input("Wat is de aanschafprijs van de elektrische auto? ")),
    onderhoudskosten = float(input("Wat zijn de onderhoudskosten van de elektrische auto? ")),
    biv = float(input("Wat is de biv van de elektrische auto? ")),
    verkeersbelasting = float(input("Wat is de verkeersbelasting van de elektrische auto? ")),
    verzekering = float(input("Wat is de verzekering van de elektrische auto? ")),
    brandstofkosten = float(input("Wat zijn de brandstofkosten van de elektrische auto? ")),
    verbruik = float(input("Wat is het verbruik van de elektrische auto? ")) / 100,
    maximale_leeftijd = float(input("Wat is de maximale leeftijd van de elektrische auto? ")),
    afstand_lege_tank = float(input("Wat is de afstand tot de lege tank van de elektrische auto? ")),
    uitstoot = float(input("Wat is de uitstoot van de elektrische auto? ")),
    uitstoot_productie = float(input("Wat is de uitstoot_productie van de elektrische auto? "))
)

Auto_Benzine = Auto(
    naam = input("Wat is de naam van de benzine auto? "),
    aanschafprijs = float(input("Wat is de aanschafprijs van de benzine auto? ")),
    onderhoudskosten = float(input("Wat zijn de onderhoudskosten van de benzine auto? ")),
    biv = float(input("Wat is de biv van de benzine auto? ")),
    verkeersbelasting = float(input("Wat is de verkeersbelasting van de benzine auto? ")),
    verzekering = float(input("Wat is de verzekering van de benzine auto? ")),
    brandstofkosten = float(input("Wat zijn de brandstofkosten van de benzine auto? ")),
    verbruik = float(input("Wat is het verbruik van de benzine auto? ")) / 100,
    maximale_leeftijd = float(input("Wat is de maximale leeftijd van de benzine auto? ")),
    afstand_lege_tank = float(input("Wat is de afstand tot de lege tank van de benzine auto? ")),
    uitstoot = float(input("Wat is de uitstoot van de benzine auto? ")),
    uitstoot_productie = float(input("Wat is de uitstoot_productie van de benzine auto? "))
)

afstand_per_jaar = 15000
jaar_rijden = int(input("Hoeveel jaar wil je de auto rijden? "))

Auto_Elektrisch_co2 = Auto_Elektrisch.totale_uitstoot(afstand_per_jaar, jaar_rijden) / 1000
Auto_Benzine_co2 = Auto_Benzine.totale_uitstoot(afstand_per_jaar, jaar_rijden) / 1000

Auto_Elektrisch_kosten = Auto_Elektrisch.totale_kosten(afstand_per_jaar, jaar_rijden)
Auto_Benzine_kosten = Auto_Benzine.totale_kosten(afstand_per_jaar, jaar_rijden)

print("\n================= VERGELIJKING ELEKTRISCH VS BENZINE =================\n")
print(f"Periode: {jaar_rijden} jaar | Afstand per jaar: {afstand_per_jaar} km\n")

print("CO₂-UITSTOOT (in kg)")
print("------------------------------------------------------------------")
print(f"{Auto_Elektrisch.naam:20}: {Auto_Elektrisch_co2:,.1f} kg")
print(f"{Auto_Benzine.naam:20}: {Auto_Benzine_co2:,.1f} kg")
print("------------------------------------------------------------------")
print("Opmerking: De Tesla stoot geen CO₂ uit tijdens het rijden.\n")

print("TOTALE KOSTEN (in euro)")
print("------------------------------------------------------------------")
print(f"{Auto_Elektrisch.naam:20}: €{Auto_Elektrisch_kosten:,.2f}")
print(f"{Auto_Benzine.naam:20}: €{Auto_Benzine_kosten:,.2f}")
print("------------------------------------------------------------------")

verschil = Auto_Benzine_kosten - Auto_Elektrisch_kosten
if verschil > 0:
    print(f"De Tesla is over deze periode €{verschil:,.2f} goedkoper.")
else:
    print(f"De Mustang is over deze periode €{abs(verschil):,.2f} goedkoper.")

print("\n==================================================================\n")