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
            attackChoice = player.ChoiceAttack()
            print(player.attack)
        else:
            attackChoice = input("Choose your attack : ")
        player.attack = attackChoice.lower()
        attackChoice = input("Choose your attack : ")
        player1.attack = attackChoice.lower()
        player.attack.lower()
        player1.attack.lower()
        player1.fight(player)


        print(player.name, "has: ", player.win, " points !")
        print(player1.name, "has: ", player1.win, " points !")

    if (player.win == 3):
        print(player.name, ", win !")
        player.gameWin += 1
    else:
        print(player1.name, ", win !")
        player1.gameWin += 1

    answer = input("Do you want to restart ? (yes or no)")
    answer = answer.lower()

    if answer == "no":
        restart = False
    else:
        player.win = 0
        player1.win =0







