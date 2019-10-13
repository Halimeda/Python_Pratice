from random import randint
number = randint(0, 10)
print(number)
if number > 9:
    print("Score maximum")
elif number > 5 and number < 10:
    print("Bon score")
else:
    print("Score correct")