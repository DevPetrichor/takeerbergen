getal = int(input("Geef het getal waarvan je de kwadraat wilt berekenen:\n"))
berekeningresultaat = getal ** 2
print("Het berekent getal is: ",berekeningresultaat)
print("Wil je het resultaat handmatig controleren? (Y/N) ")
antwoord = input()

if antwoord.lower() == 'y':
    print(f"Handmatig berekenen: {getal} x {getal} =", getal*getal)
    if getal*getal == berekeningresultaat:
        print("Het resultaat is correct!")          