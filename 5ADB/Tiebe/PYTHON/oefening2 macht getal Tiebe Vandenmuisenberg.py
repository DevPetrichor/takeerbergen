getal= float(input("Geef een getal: "))
#dit vraagt de gebruiker om een getal in te vullen
uitkomst= getal**2
#dit berekent het kwadraat van het getal
print("Het kwadraat van je getal is", uitkomst, ".")
#dit print het resultaat van het kwadraat
antwoord = input('wil je het resultaat controlleren? (ja/nee)')
if antwoord.lower() == 'ja':
    print('handmatig berekend is het', getal, "*", getal, "=", uitkomst)