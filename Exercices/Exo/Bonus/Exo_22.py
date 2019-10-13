nmr_count = 0
nmr_list = []

while nmr_count < 5:
    number = int(input("Saisissez un nombre : "))
    if number > 10 or number < 1:
        print("Le nombre n'est pas accepter")
    else:
        nmr_list.append(number)
        nmr_count += 1
for i in nmr_list:
    print(i)