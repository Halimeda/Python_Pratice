class Vehicle():
    def __init__(self, speed):
        self.speed = speed
        self.distance = 0
    def ride(self, duration):
        travel = duration * self.speed
        self.distance += travel

class Bike(Vehicle):
    def __init__(self):
        super().__init__(15)

class Car(Vehicle):
    def __init__(self):
        super().__init__(100)
        self.fuel = 100
        self.consumption = 0.05
    def ride(self, duration):
        travel = duration * self.speed
        travel_max = self.fuel / self.consumption
        travel = min(travel, travel_max)
        self.distance += travel
        self.fuel -= travel * self.consumption

    def fill_tank(self, fuel_volume):
        self.fuel += fuel_volume 

class Train(Vehicle):
    def __init__(self, max_passenger):
        super().__init__(150)
        self.passengers = 0
        self.max_capacity = max_passenger
    def take_on_board(self, new_passengers):
        self.passengers += new_passengers
        self.passengers = min(self.passengers, self.max_capacity)
class TrainInterCity(Train):
    def __init__(self):
        super().__init__(100)
        self.profit = 0
        self.profit_by_kilometer = 2.5
    def ride(self, duration):
        super().ride(duration)
        self.profit += self.profit_by_kilometer * self.distance

class FreightTrain(Train):
    def __init__(self):
        super().__init__(4)
        self.chargement = 0
    def add_chargement(self, charge):
        self.chargement += charge


velo = Bike()
voiture = Car()
train1 = TrainInterCity()
train2 = FreightTrain()

velo.ride(2)
voiture.ride(2)
train1.ride(50)
train2.ride(2)
print(velo.distance)
print(voiture.distance)
print(train1.distance)
print(train1.profit)
train1.take_on_board(50)
print(train1.passengers)
print(train2.distance)
train2.add_chargement(150)
print(train2.chargement)
train2.take_on_board(3)
print(train2.passengers)