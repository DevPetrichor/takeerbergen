import time

game = True
galg = 0
woord = ""
timer = 0
running = False
letter = ""
geraden = []

woord = input("Geef een woord: ").lower()
print("\n" * 50)
print("Spel starten...")
running = True

display = ["_"] * len(woord)

while running and galg < 6 and "_" in display:
    print(" ".join(display))
    print(f"Fouten: {galg}/6")
    letter = input("Raad een letter: ").lower()
    if len(letter) != 1 or not letter.isalpha():
        print("Ongeldige invoer.")
        continue
    if letter in geraden:
        print("Deze letter heb je al geraden.")
        continue
    geraden.append(letter)
    if letter in woord:
        for i in range(len(woord)):
            if woord[i] == letter:
                display[i] = letter
    else:
        galg += 1
        print("Fout!")

if "_" not in display:
    print("Gefeliciteerd! Je hebt het woord geraden:", woord)
else:
    print("Game over! Het woord was:", woord)


