naam = input("Van wat wil je de druk berekenen: ")
l = float(input("Lengte van voorwerp (m): "))
b = float(input("Breedte van voorwerp (m): "))
h = float(input("Hoogte van voorwerp (m): "))
g = float(input("Gewicht van voorwerp (kg): "))
p = float(input("Hoeveel druk wil je (bar): "))
oppervlakte = float(input("Oppervlakte van de ondergrond waar de bananen op liggen (m²): "))

pa = p * 10**5
F = g * 9.81
A = b * h
druk = F / A
n = round((pa * oppervlakte) / (F))
oppervlakte_uitkomst = oppervlakte / A

print(f"Je zult {n} {naam}(en) nodig hebben voor een druk van {p} bar.")
print(f"Je kunt {int(oppervlakte_uitkomst)} {naam} op de opgegeven ondergrond plaatsen.")

