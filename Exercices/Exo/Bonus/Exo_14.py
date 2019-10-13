from random import randint
hp_monster = 30
print(hp_monster)
while hp_monster > 0:
    attack = randint(5, 10)
    hp_monster = hp_monster - attack
    if hp_monster > 0:
        print("Il reste " + str(hp_monster) + " point de vie au monstre !")
    else:
        print("Félicitation ! Tu as vaincu le monstre")