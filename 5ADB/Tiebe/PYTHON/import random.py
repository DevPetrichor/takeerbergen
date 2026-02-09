import random
dobbelsteen_1 = random.randint(1, 6)
dobbelsteen_2 = random.randint(1, 6)
dobblesteen_3 = random.randint(1, 6)
# dit vraagt een willekeurig getal tussen 1 en 6 voor alle drie dobbelstenen
if dobbelsteen_1 == dobbelsteen_2 == dobblesteen_3:
     # dit controleert of alle drie de dobbelstenen hetzelfde getal hebben
    print("Drie gelijke! ", dobbelsteen_1, dobbelsteen_2, dobblesteen_3)
elif dobbelsteen_1 == dobbelsteen_2 or dobbelsteen_1 == dobblesteen_3 or dobbelsteen_2 == dobblesteen_3:
    # dit controleert of er twee dobbelstenen hetzelfde getal hebben
    print("Twee gelijke! ", dobbelsteen_1, dobbelsteen_2, dobblesteen_3)
else:    print("Geen gelijke! ", dobbelsteen_1, dobbelsteen_2, dobblesteen_3)
# dit geeft aan dat er geen gelijke dobbelstenen zijn
