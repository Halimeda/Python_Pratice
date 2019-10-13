def plant_height(year):

    if year == 1:
        return 0.8
    else:
        return plant_height(year - 1) * 1.5


print(plant_height(1))
print(plant_height(2))
print(plant_height(3))
print(plant_height(4))