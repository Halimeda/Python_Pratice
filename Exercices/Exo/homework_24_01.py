number = int(input("Entrez un chiffre : "))
nbr_list = [number]
how_much = 1
result = number

while result < 20:
    number = int(input("Entrez un chiffre : "))
    nbr_list.append(number)
    result = result + number
    how_much += 1
if result >= 20:
    for i in range(len(nbr_list) - 1):
        big = max(nbr_list[i], nbr_list[i +1])
        small = min(nbr_list[i], nbr_list[i +1])
print("Plus grand chiffre proposé : " + str(big))
print("Plus petit chiffre proposé : " + str(small))
print("Nombre de proposition : " + str(how_much))