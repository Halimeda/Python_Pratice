from random import randint
bomb = randint(1, 6)
if bomb == 4 or bomb == 3:
    print("Boum !")
else:
    print("Rien ne se passe ...")