from random import choice

alphabet = "abcdefghijklmnopqrstuvwxyz"
character = choice(alphabet)
error = 0

for n in range(5)
    character = choice(alphabet)
    ask = None
    while ask != character:
        ask = input("Tapez la lettre suivante : " + character + " ")
        if ask != character:
            error += 1
    print("Vous avez commis " + str(error) + " erreurs")
   # again = input("Voulez vous continuez ? (Répondez 'o' ou 'n') ")
    #if again == "o" or again == "O":
     #   error = 0
    #else:
     #   essai = -1