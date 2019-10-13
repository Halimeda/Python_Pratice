inventory = {"Pouvoir" : 10, "Magie" : 5, "Défense" : 3}
inventory["Nom"] = input("Héro, quel est ton nom ? ")

for key, value in inventory.items():
    print(key + " : " + str(value))