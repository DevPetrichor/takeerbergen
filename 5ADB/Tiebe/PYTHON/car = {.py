car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car[input('Enter key: ')] = input('Enter value: ')

print(x) #after the change
