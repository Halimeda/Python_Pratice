class Choice:
    def __init__(self, name):
        self.name = name
        
    def fight (self, choice):
        if self.name == choice.name:
            print("Égalité, rejoué")
        elif ((self.name == "Rock" or choice.name == "Rock") and (self.name == "Paper" or choice.name == "Paper")):
            print("Paper Win!")
        elif ((self.name == "Scissors" or choice.name == "Scissors") and (self.name == "Paper" or choice.name == "Paper")):
            print("Scissors Win!")
        else:
            print("Rock win")

class Paper(Choice):
    def __init__(self):
        self.name = "Paper"

class Scissor(Choice):
    def __init__(self):
        self.name = "Scissors"

class Rock(Choice):
    def __init__(self):
        self.name = "Rock"
