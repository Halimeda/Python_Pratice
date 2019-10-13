number = int(input("Saisissez un nombre : "))
number_list = [number]
big = 0
small = 0
while number != 0:
    number = int(input("Saisissez un nombre : "))
    number_list.append(number)
for i in range(len(number_list)):
    big = max((number_list[i]), big)
    small = min((number_list[i]), small)
print(big)
print(small)