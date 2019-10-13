from random import randint

essai = 3
number = randint(1, 10)
player = int(input("Devinez un chiffre entre 1 et 10. "))

if (player == number):
    print("You Win!")
elif (player > number):
    essai = essai - 1
    print("Le chiffre est plus petit")
    player = int(input("Devinez un chiffre entre 1 et 10." + "Il reste " + str(essai) + " chance ! "))
    if (player == number):
        print("You Win!")
    elif (player > number):
        essai = essai - 1
        print("Le chiffre est plus petit")
        player = int(input("Devinez un chiffre entre 1 et 10. " + "Il reste " + str(essai) + " chance ! "))
        if (player == number):
            print("You Win!")
        else:
            print("You loose. The number was " + str(number) + " Try again !")
    else:
        essai = essai - 1
        print("Le chiffre est plus grand")
        player = int(input("Devinez un chiffre entre 1 et 10. " + "Il reste " + str(essai) + " chance ! "))
        if (player == number):
            print("You Win!")
        else:
            print("You loose. The number was " + str(number) + " Try again !")
else:
    essai = essai - 1
    print("Le chiffre est plus grand")
    player = int(input("Devinez un chiffre entre 1 et 10. " + "Il reste " + str(essai) + " chance ! "))
    if (player == number):
        print("You Win!")
    elif (player > number):
        essai = essai - 1
        print("Le chiffre est plus petit")
        player = int(input("Devinez un chiffre entre 1 et 10. " + "Il reste " + str(essai) + " chance ! "))
        if (player == number):
            print("You Win!")
        else:
            print("You loose. The number was" + str(number) + " Try again !")
    else:
        essai = essai - 1
        print("Le chiffre est plus grand")
        player = int(input("Devinez un chiffre entre 1 et 10. " + "Il reste " + str(essai) + " chance ! "))
        if (player == number):
            print("You Win!")
        else:
            print("You loose. The number was " + str(number) + " Try again !")