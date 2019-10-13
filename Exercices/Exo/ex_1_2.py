from random import choice

characters = ["A", "B", "C", "D", "E", "F", "G"] # liste raccourcie de l'alphabet.

number_of_errors = 0

for n in range(5):
    character = choice(characters)
    entry = None

    while(entry != character):
        entry = input("Tapez " + character + ": ")
        number_of_errors = number_of_errors + 1

    number_of_errors = number_of_errors - 1

print("Nombre d'erreurs: " + str(number_of_errors))