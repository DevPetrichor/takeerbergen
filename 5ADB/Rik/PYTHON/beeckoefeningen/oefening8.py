fruit = {"appel": 2.5, "banaan": 1.80, "peer": 2.20}
fruit = str(input("Welk fruit wil je kopen? "))
if fruit in fruit:
    gewicht = float(input("Hoeveel kg wil je kopen? "))
    prijskg = fruit[fruit]
    totaalprijs = gewicht * prijskg
    print(f"De totaalprijs voor {gewicht} kg {fruit} is {totaalprijs} euro.")
else:
    print("Sorry, dat fruit hebben we niet.")


