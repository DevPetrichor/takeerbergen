keuze=int(input("""Kies een optie:
 oefening 1:Opgave herhaling for and while
 oefening 2:Opgave voorschot berekenen
 oefening 3: Opgave gewicht omzetten
 """))
if keuze==1:
    a=1
    for i in range(1,6):
        print(i)
        
    while a< 6:
        print(a)
        a += 1

if keuze==2:
    prijsHuis = float(input("Wat is de prijs van het huis? "))
    WaardeBankRekening = float(input("Wat is de waarde van je bankrekening? "))
    if WaardeBankRekening >= prijsHuis/4:
        if WaardeBankRekening > prijsHuis:
            print(f"Je moet 10% van het bedrag betalen wat neerkomt op {prijsHuis*0.10} euro")
        else:
            print(f"Je moet 20% van het bedrag betalen wat neerkomt op {prijsHuis*0.20} euro")
    else:
        print("Je hebt niet genoeg geld om het huis te kopen!")
if keuze==3:
    gewicht=float(input("Wat is het gewicht "))
    eenheid=input("Wat is de eenheid? (kg of lbs)")
    if eenheid == "kg":
        print(f"{gewicht} kg is gelijk aan {gewicht*2.2} lbs")
    elif eenheid == "lbs":
        print(f"{gewicht} lbs is gelijk aan {gewicht/2.2} kg")
    else:
        print("Ongeldige eenheid, voer 'kg' of 'lbs' in.")
    