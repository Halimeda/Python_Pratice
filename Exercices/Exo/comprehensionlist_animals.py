animals = ["Giraffe", "Dauphin", "Ecureuil", "Dragon", "Zebre", "Chat", "Chien"]
letter =["C", "D", "E"]
# second = [animal for animal in animals if animal[0] == "C" or animal[0] == "D" or animal[0] == "E"]
# second = [animal for animal in animals for x in letter if letter animal[0] == x]
second_list = [animal for animal in animals if animal[0].upper in letter]

print(second_list)