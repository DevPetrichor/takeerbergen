import random
a = random.randint(1, 6)  # Genereer een willekeurig getal tussen 1 en 6
b = random.randint(1, 6)  # Genereer een willekeurig getal tussen 1 en 6
c = random.randint(1, 6)  # Genereer een willekeurig getal tussen 1 en 6

print(f"De worpen zijn: {a}, {b}, {c}")  # Print de gegooide getallen

if a == b == c:
    print(f"Je hebt drie dezelfde getallen!") # Drie dezelfde getallen
elif a == b or a == c or b == c:
    print(f"Je hebt twee dezelfde getallen!") # Twee dezelfde getallen
else:
    print(f"Alle worpen zijn verschillend!") # Geen dezelfde getallen

# De worpen volgen een opeenvolging
if (a + 1 == b and b + 1 == c) or (a - 1 == b and b - 1 == c) or \
    (b + 1 == a and a + 1 == c) or (b - 1 == a and a - 1 == c) or \
    (c + 1 == a and a + 1 == b) or (c - 1 == a and a - 1 == b): # Controleer opeenvolging
    print("De worpen volgen een opeenvolging!")
else:
    print("De worpen volgen geen opeenvolging.")
