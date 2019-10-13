from random import choice

characters = ["A", "B", "C", "D", "E", "F", "G"] # liste raccourcie de l'alphabet.

character = choice(characters)

entry = None

while(entry != character):
    entry = input("Tapez " + character + ": ")   