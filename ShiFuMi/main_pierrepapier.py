from Player import *


number = int(input("How many players are you ? (1 or 2) : "))
restart = True
answer = ""

if (number%2 != 0):
    player = Computer()
    player1 = Player(input("Enter a player name : "))
else:
    player = Player(input("Enter a player name : "))
    player1 = Player(input("Enter a player name : "))


while restart:

    while (player.win < 3 and player1.win < 3):

        if (number == 1):
            player.ChoiceAttack()
            print(player.attack)
        else:
            player.attack = input("Choose your attack : ")
        player1.attack = input("Choose your attack : ")

        player1.fight(player)


        print(player.name, "has: ", player.win, " points !")
        print(player1.name, "has: ", player1.win, " points !")

    if (player.win == 3):
        print(player.name, ", win !")
    else:
        print(player1.name, ", win !")

    answer = input("Do you want to restart ? (yes or no)")

    if answer == "no":
        restart = False






