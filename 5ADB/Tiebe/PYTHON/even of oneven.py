getal_1=int(input('geef een getal dat je wilt controleren: '))
getal_2=int(input('geef een tweede getal dat je wilt controleren: '))
if getal_1 and getal_2 % 2==0:
    print('getal 1 en getal 2 zijn even')
elif getal_1 % 2==0 and getal_2 % 2!=0:
    print('getal 1 is even en getal 2 is oneven')
elif getal_1 % 2!=0 and getal_2 % 2==0:
    print('getal 1 is oneven en getal 2 is even')
else:
    print('getal 1 en getal 2 zijn oneven')