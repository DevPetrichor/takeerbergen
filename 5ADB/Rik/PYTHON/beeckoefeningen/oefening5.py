jaar = int(input("Geef het jaar dat je wilt controleren of het een schrikkeljaar is: ")) # vraag de gebruiker om een jaartal in te voeren
if (int(jaar) % 4 == 0 and int(jaar) % 100 != 0): # controleer of het jaartal deelbaar is door 4 en niet deelbaar is door 100
    if (int(jaar) % 400 != 0): # controleer of het jaartal niet deelbaar is door 400
        print (f"{jaar} is een schrikkeljaar.") 
else:   
    print (f"{jaar} is geen schrikkeljaar.")