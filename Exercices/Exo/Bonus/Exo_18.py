from random import randint
number = -1
number_list = []
condition = False
while condition == False:
    number = randint(0, 10)
    number_list.append(number)
    if len(number_list) > 1:
        if number_list[len(number_list) - 1] == number_list[len(number_list) - 2]:
            condition = True
del number_list[len(number_list) - 1]
for i in number_list:
    print(i)
