class auto:
    def __init__(self, aankoopPrijs, onderhoud, biv, verzekering, brandstof, kilometers, verkeersBelasting):
        self.aankoopPrijs = aankoopPrijs
        self.onderhoud = onderhoud
        self.biv = biv
        self.verzekering = verzekering
        self.brandstof = brandstof
        self.kilometers = kilometers
        self.verkeersBelasting = verkeersBelasting
    def energiePerJaar(self):
        return self.brandstof * (self.kilometers / 15)
    def totaalKM(self, totaalJaar):
        return self.kilometers * totaalJaar
    def prijsEersteJaar(self, totaalJaar):
        return self.aankoopPrijs + self.onderhoud + self.biv + self.verzekering + self.energiePerJaar() + self.verkeersBelasting
    def prijsVervolgJaar(self, totaalJaar):
        return self.onderhoud + self.verzekering + self.energiePerJaar() + self.verkeersBelasting
    def totaalPrijs(self, totaalJaar):
        return self.prijsEersteJaar(totaalJaar) + self.prijsVervolgJaar(totaalJaar) * (totaalJaar - 1)
    def prijsPerKM(self, totaalJaar):
        return self.totaalPrijs(totaalJaar) / self.totaalKM(totaalJaar)
    def printPrijs(self, totaalJaar):
        for jaar in range(1, totaalJaar + 1):
            if jaar == 1:
                print(f"Jaar {jaar}: Prijs = {self.prijsEersteJaar(totaalJaar):.2f}")
            else:
                uitgerekend = self.prijsVervolgJaar(totaalJaar) + self.prijsVervolgJaar(totaalJaar) * (jaar - 1)
                print(f"Jaar {jaar}: Prijs = {uitgerekend:.2f}")
        print("De totale prijs van de auto over", totaalJaar, "jaar is:", f"{self.totaalPrijs(totaalJaar):.2f}")
        print("De prijs per jaar is:", f"{self.totaalPrijs(totaalJaar) / totaalJaar:.2f}")
        print("De prijs per kilometer is:", f"{self.prijsPerKM(totaalJaar):.2f}")
        print(f"Prijs eerste jaar: {self.prijsEersteJaar(totaalJaar):.0f}")
        print(f"Prijs vervolgjaar: {self.prijsVervolgJaar(totaalJaar):.0f}")
    def __str__(self):
        return f"Aankoopprijs: {self.aankoopPrijs}, Onderhoud: {self.onderhoud}, BIV: {self.biv}, Verzekering: {self.verzekering}, Brandstof: {self.brandstof}, Kilometers: {self.kilometers}, Verkeersbelasting: {self.verkeersBelasting}"


# aankoopPrijs, onderhoud, biv, verzekering, brandstof, kilometers, verkeersBelasting
elektrischeAuto = auto(31895, 350, 61.5, 1170, 0.3306, 15000, 102.96)
benzineAuto = auto(31.499, 804, 0, 1.248, 1.861, 15000, 250.4)

print("Elektrische Auto:")
elektrischeAuto.printPrijs(17)
print("\nBenzine Auto:")
benzineAuto.printPrijs(17)