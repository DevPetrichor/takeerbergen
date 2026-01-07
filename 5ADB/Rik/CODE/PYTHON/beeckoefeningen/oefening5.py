jaar = int(input("Geef het jaar dat je wilt controleren of het een schrikkeljaar is: "))
if (int(jaar) % 4 == 0 and int(jaar) % 100 != 0):
    if (int(jaar) % 400 != 0):
        print (f"{jaar} is een schrikkeljaar.")
else:
    print (f"{jaar} is geen schrikkeljaar.")