import random
mogelijkheden = ['schaar', 'steen', 'papier']
while True:
    computer=random.choice(mogelijkheden)
    speler=input('kies schaar, steen of papier of stop: ').lower()
    if speler == 'stop':
        print('Spel gestopt.')
        break
    if speler not in mogelijkheden:
        print('Ongeldige keuze, probeer opnieuw.')
        continue
    if speler == computer :
     print('Gelijkspel. De computer koos', computer,'.')
    elif speler == 'schaar'and computer == 'papier' or speler == 'steen'and computer == 'papier' or speler == 'papier'and computer == 'steen':
     print('Je hebt gewonnen. De computer koos', computer,'.')
    else :
     print('Je hebt verloren. De computer koos', computer,'.')