from random import randint

def bingo():
   print("Bingo !!!!!!!!")

def ask_number():
    number = int(input("Devine un chiffre entre 1 et 10. "))
    return (number)

def verify_number(number, player):
    if (player < number):
        print("Le chiffre est plus grand")
    elif (player > number):
        print("Le chiffre est plus petit")
    else:
        bingo()
        essai == 0
        return (True)
    return (False)

essai = 3
number = randint(1, 10)
verify = False

while (verify == False and essai > 0):
    player = ask_number()
    essai -= 1
    verify = verify_number(number, player)
    if (essai > 0 and verify == False):
        print("Il reste te " + str(essai) + " chance(s) !")
    if ((essai == 0) and (verify == False)):
        print("Perdu ! Le chiffre était " + str(number) + ". Essaye encore !")