from car import Car

print("---------------------------------------")
print("GARAGE")
print("---------------------------------------")
garage_groote = int(input("Hoe groot is je garage? "))
garage = []

while True:
    antwoord = input("Wil je een auto registreren? (Ja/Nee): ").lower()
    if antwoord != "ja":
        break

    if len(garage) >= garage_groote:
        antwoord3 = int(input("Garage is vol! Specifieke auto verkopen? (Geef nummer in): "))
        if 0 < antwoord3 <= len(garage):  
            index = antwoord3 - 1
            auto = garage[index]
            garage.remove(auto)
            print(f"{auto} succesvol verwijderd uit de garage. De garage bevat nog {len(garage)} auto's.")
            print("---------------------------------------")
        else:
            print("Ongeldige invoer, probeer opnieuw.")
    else:
        nieuwe_auto = Car.krijg_info_car()
        garage.append(nieuwe_auto)
        print("Auto werd succesvol geregistreerd!")
        print("---------------------------------------")  
        

print(len(garage),"Geregistreerde auto's:")
print("---------------------------------------")
for auto in garage:
    print(auto.krijg_info())