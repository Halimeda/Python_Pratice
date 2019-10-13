number = int(input("Entrez un chiffre : "))
nbr_list = (number)
how_much = 1
big = None
small = None
print("a")
while number < 20:
    number = int(input("Entrez un chiffre : "))
    nbr_list.append(number)
    how_much += 1
for i in len(nbr_list):
    result = result + nbr_list[i]
    while i < (len(nbr_list) - 1):
        big = max(nbr_list[i], nbr_list[i +1])
        small = min(nbr_list[i], nbr_list[i +1]

print("Nombre de chiffre entré : " + str(how_much))
print("Plus grand chiffre" + str(big))
print("Plus petit chiffre" + str(small))
