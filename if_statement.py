car='BMW'
cars = ['subaru', 'audi', 'BMW']

print(car not in cars, False)
print(car == 'subaru', False)
print(car is 'aidu', False)
print(car == 'Burger' or 1 < 0, False)
print(1 < 0 and 1 == 1, False)

print(car in cars, True)
print(car == 'BMW', True)
print(car is not 'aidu', True)
print(car != 'aidu', True)
print(len(car) > len('au'), True)

print(car == 'BMW'.lower(), False)
