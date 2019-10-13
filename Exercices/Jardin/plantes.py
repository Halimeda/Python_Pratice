from random import randint
class Garden():

    def __init__(self):
        self.plant =[]
        self.money = 0

    def water(self, flower):
        flower.water = False
        water = randint(1, 4)
        if water != 4:
            return(True)
    
    def plants(self, flower):
        self.plant = []
        while len(self.plant) < 5:
            self.plant.append(flower)
    
    def cut(self, flower):
        if flower.grow == flower.max_grow:
            self.money += flower.price
            flower.grow = 0
            self.plant.remove(flower)


class Flower(Garden):
    def __init__(self, flower, price):
        self.width = 0
        self.grow = flower
        self.maxgrow = 10
        self.price = price

    def max_grow(self):
        if self.width == self.maxgrow:
            return(True)
        return(False)

    def growing(self):
        maturate = self.max_grow()
        if maturate == True:
            return ()
        watering = super().water()
        if watering == True:
            self.width += self.grow
            self.water = False
        else:
            self.width += self.grow/2
        self.width = min(self.width, self.maxgrow)

class Rose(Flower):
    def __init__(self):
        super().__init__(1.1, 5)
        self.name = "Rose"

    def __repr__(self):
        return (self.name + "\n")

    def growing(self):
        watering = super.water()
        if watering == False:
            self.price -= 0.2
        super.grow()

class Tulip(Flower):
    def __init__(self):
        super().__init__(1.2, 6)
        self.name = "Tulipe"

    def __repr__(self):
        return (self.name + "\n")

    def growing(self):
        watering = super.water()
        if watering == True:
            super().grow()

class Lila(Flower):
    def __init__(self):
        super().__init__(0.6, 3)
        self.name = "Lila"

    def __repr__(self):
        return (self.name + "\n")

    def growing(self):
        super().grow()

gain = 0
jardin = Garden()
while gain < 100:
    plant_choice = randint(1 ,3)
    if plant_choice == 1:
        jardin.plants(Rose)
    elif plant_choice == 2:
        jardin.plants(Tulip)
    else:
        jardin.plants(Lila)
    gain += 10


for i in range(len(jardin.plant)):
    print(jardin.plant)
    print("\n")