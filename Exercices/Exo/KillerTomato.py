from random import randint

class KillerTomato:
    def __init__(self):
        self.hp = 10
        self.hp_max = 10
        self.defense = 1
    def attack(self, other_vegetable):
        damage = max(0, randint(4, 6) - other_vegetable.defense)
        other_vegetable.hp -= damage

class PuncherBrocoli:
    def __init__(self):
        self.hp = 10
        self.hp_max = 10
        self.defense = 2
    def attack(self, other_vegetable):

        if self.hp < (self.hp_max/2):
            damage = randint(1, 4) * 2
        else:
            damage = randint(1, 4)
        damage -= other_vegetable.defense
        other_vegetable.hp -= damage

class BrawlerCarrot:
    def __init__(self):
        self.hp = 9
        self.hp_max = 9
        self.defense = 1
    def attack(self, other_vegetable):
        damage = randint(3, 5)
        if damage == 5 and self.hp < self.hp_max:
            self.hp += 1
        damage = max(0, (damage - other_vegetable.defense ))
        other_vegetable.hp -= damage

class Ring:

    def __init__(self, veg_1, veg_2):
        self.change_vegetables(veg_1, veg_2)

    def change_vegetables(self, veg_1, veg_2):
        self.veg1 = veg_1
        self.veg2 = veg_2

    def fight_round(self):

        self.veg1.attack(self.veg2)
        if self.veg2.hp <= 0:
            return (self.veg1)
        self.veg2.attack(self.veg1)
        if self.veg1.hp <= 0:
            return (self.veg2)
        print("HP Fighter 1 : " + str(self.veg1.hp))
        print("HP Fighter 2 : " + str(self.veg2.hp))
        return (None)

    def combat(self):
        while self.fight_round() == None:
            self.fight_round()
        if self.fight_round() == self.veg1:
            return (self.veg1)
        elif self.fight_round() == self.veg2:
            return (self.veg2)
        #winner = None
        #while winner == None: 
        #   winner = self.fight_round()
        #return (winner)



tomato = KillerTomato()
brocoli = PuncherBrocoli()
carrot = BrawlerCarrot()

fight1 = Ring(tomato, brocoli)
print(fight1.combat())

tomato.hp = tomato.hp_max
brocoli.hp = brocoli.hp_max

print(fight1.combat())

tomato.hp = tomato.hp_max
brocoli.hp = brocoli.hp_max

fight2 = Ring(carrot, tomato)
print(fight2.combat())

tomato.hp = tomato.hp_max
carrot.hp = carrot.hp_max

print(fight2.combat())

carrot.hp = carrot.hp_max

fight3 = Ring(brocoli, carrot)
print(fight3.combat())

brocoli.hp = brocoli.hp_max
carrot.hp = carrot.hp_max

print(fight3.combat())