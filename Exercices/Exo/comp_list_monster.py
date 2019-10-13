from random import randint

class Monster():
    def __init__(self):
        self.hp = randint(20, 35)
        self.attack = randint(1, 6)

#Permet d'afficher une description/représentation de l'objet
    def __repr__(self):
        return ("HP : " + str(self.hp) + "  Attack : " + str(self.attack) + "\n")

monsters = []
for i in range(5):
    monsters.append(Monster())
print(monsters)
good_one = [monster for monster in monsters if monster.hp >= 25 and monster.attack >= 2]
print(good_one)
print("Sorted")
condition = True
while condition:
    condition = False
    for i in range(len(good_one) - 1):
        if good_one[i].attack > good_one[i + 1].attack:
            temp = good_one[i]
            good_one[i] = good_one[i + 1]
            good_one[i + 1] = temp
            condition = True
print(good_one)