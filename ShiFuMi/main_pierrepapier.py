from Choice_possibility import *
from Player import *

player = Player(input("Entrez un nom de joueur : "))
computer = Computer()

computer = computer.ChoiceAttack()
player.attack = input("entrez un choix")

computer.fight(player)

choice = Rock()
choice2 = Scissor()
choice3 = Paper()
choice.fight(choice3)
choice.fight(choice2)
choice2.fight(choice)
choice.fight(choice)

