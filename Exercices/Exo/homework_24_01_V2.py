number = int(input("Entrez un chiffre : "))
nbr_list = [number]
how_much = 1
result = number
big = -1
small = 10

while result < 20:
    number = int(input("Entrez un chiffre : "))
    nbr_list.append(number)
    result = result + number
    how_much += 1
for i in nbr_list:
    big = max(i, big)
    small = min(i, small)
    print(i)
print("Plus grand chiffre proposé : " + str(big))
print("Plus petit chiffre proposé : " + str(small))
print("Nombre de proposition : " + str(how_much))