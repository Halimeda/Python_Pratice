
numbers = []

while sum(numbers) < 20:
    number = input('Donne moi un nombre: ')
    number = int(number)
    numbers.append(number)

print('Nombre d''entrées: ' + str(len(numbers)))
print('Plus petit nombre: ' + str(min(numbers)))
print('Plus grand nombre: ' + str(max(numbers)))
