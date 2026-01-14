import math
#dit importeert de math module 
getal= float(input("geef een getal om de vierkantswortel van te berekenen: "))
#dit vraagt de gebruiker voor een getal
uitkomst=math.sqrt(getal)
#dit berekent de vierkantswortel van het getal
if getal == 0:
    print("de vierkantswortel van 0 is niet gedefinieerd")
    #dit is voor als het getal 0 is
else :
    print("de vierkantswortel van", getal, "is", uitkomst)
    #dit print de uitkomst van de vierkantswortel