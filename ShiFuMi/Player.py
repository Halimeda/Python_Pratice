from random import randint

class PlayerType:

    def __init__(self, name):
        self.name = name
        self.win = 0
        self.attack =""
        self.choice = ["rock", "paper", "scissors"]
    
    def fight (self, player):
        if self.attack == player.attack:
            print("Égalité, rejoué")
        elif ((self.attack == "rock" or player.attack == "rock") and (self.attack == "paper" or player.attack == "paper")):
            print("Paper Win!")
            if(self.attack == "paper"):
                self.win += 1
            else:
                player.win += 1
        elif ((self.attack == "scissors" or player.attack == "scissors") and (self.attack == "paper" or player.attack == "paper")):
            print("Scissors Win!")
            if(self.attack == "scissors"):
                self.win += 1
            else:
                player.win += 1
        else:
            print("Rock win")
            if(self.attack == "rock"):
                self.win += 1
            else:
                player.win += 1


class Computer(PlayerType):
    def __init__(self):
        self.name = "Computer"
        super().__init__(self.name)
    
    def ChoiceAttack(self):
        number = randint(0,2)
        
        self.attack = self.choice[number]

        return self.attack


class Player(PlayerType):
    def __init__(self, player_name):
        self.name = player_name
        super().__init__(self.name)
