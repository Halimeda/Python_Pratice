from Player import *


number = int(input("How many players are you ? (1 or 2) : "))

if (number%2 != 0):
    player = Computer()
    player1 = Player(input("Entrez un nom de joueur : "))
else:
    player = Player(input("Entrez un nom de joueur : "))
    player1 = Player(input("Entrez un nom de joueur : "))


while (player.win < 3 and player1.win < 3):
    if (number == 1):
        player.ChoiceAttack()
        print(player.attack)
    else:
        player.attack = input("Choisissez une attaque : ")
    player1.attack = input("Choisissez une attaque : ")

    print(player.win)
    print(player1.win)

    player1.fight(player)


    print(player.win)
    print(player1.win)

if (player.win ==3):
    print(player.name, " , win !")
else:
    print(player1.name, " , win !")






