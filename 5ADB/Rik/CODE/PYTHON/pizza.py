def berekening_pizza(dia, prijs):
    return prijs / ((dia / 2) ** 2 * 3.1415)

diameter1 = int(input("Diameter pizza 1 (cm): "))
prijs1 = int(input("Prijs pizza 1 (euro): "))
diameter2 = int(input("Diameter pizza 2 (cm): "))
prijs2 = int(input("Prijs pizza 2 (euro): "))

prijs1_cm2 = berekening_pizza(diameter1, prijs1)
prijs2_cm2 = berekening_pizza(diameter2, prijs2)

print(f"Pizza 1 kost {prijs1_cm2:.4f} euro per cm²")
print(f"Pizza 2 kost {prijs2_cm2:.4f} euro per cm²")
print("Pizza 1 is goedkoper!" if prijs1_cm2 < prijs2_cm2 else "Pizza 2 is goedkoper!")