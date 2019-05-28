from random import randint

class PlayerType:

    def __init__(self, name):
        self.name = name
        self.win = 0
        self.attack =""

class Computer(PlayerType):
    def __init__(self):
        self.name = "Computer"
        super().__init__(self.name)
    
    def ChoiceAttack(self):
        number = randint(0,3)

        if number == 1:
            self.attack = "Paper"
        elif number == 2:
            self.attack = "Scissors"
        elif number == 3:
            self.attack = "Rock"
        
        return self.attack


class Player(PlayerType):
    def __init__(self, player_name):
        self.name = player_name
        super().__init__(self.name)
