jaar=int(input("Geef een jaartal in dat je wil checken: "))#dit vraagt de gebruiker om een jaartal in te voeren
if (jaar % 4 == 0 and jaar % 100 != 0) or (jaar % 400 == 0):#dit controleert of het jaartal een schrikkeljaar is
    print(f"{jaar} is een schrikkeljaar.")#als het een schrikkeljaar is, wordt dit bericht weergegeven
else:
    print(f"{jaar} is geen schrikkeljaar.")#als het geen schrikkeljaar is, wordt dit bericht weergegeven
