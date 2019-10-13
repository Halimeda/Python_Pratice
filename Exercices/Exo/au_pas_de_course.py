from random import randint

coureur1 = {'Name' : 'A', 'Speed' : 5, 'Distance' : 0}
coureur2 = {'Name' : 'B', 'Speed' : 5, 'Distance' : 0}
coureur3 = {'Name' : 'C', 'Speed' : 5, 'Distance' : 0}

distance = None

while coureur1['Distance'] < 100 and coureur2['Distance'] < 100 and coureur3['Distance'] < 100:
    bonus_distance = randint(2, 6)
    hurt = randint(0, 2)
    if hurt == 0:
        coureur1['Distance'] = (coureur1['Distance'] + coureur1['Speed'] + bonus_distance) / 2
    else:
        coureur1['Distance'] = coureur1['Distance'] + coureur1['Speed'] + bonus_distance

    bonus_distance = randint(2, 6)
    hurt = randint(0, 2)
    if hurt == 0:
        coureur2['Distance'] = (coureur2['Distance'] + coureur2['Speed'] + bonus_distance) / 2
    else:
        coureur2['Distance'] = coureur2['Distance'] + coureur2['Speed'] + bonus_distance

    bonus_distance = randint(2, 6)
    hurt = randint(0, 2)
    if hurt == 0:
        coureur3['Distance'] = (coureur3['Distance'] + coureur3['Speed'] + bonus_distance) / 2
    else:
        coureur3['Distance'] = coureur3['Distance'] + coureur3['Speed'] + bonus_distance

print(coureur1['Name'] + " a parcouru : " + str(int(coureur1['Distance'])) + " mètres")
print(coureur2['Name'] + " a parcouru : " + str(int(coureur2['Distance'])) + " mètres")
print(coureur3['Name'] + " a parcouru : " + str(int(coureur3['Distance'])) + " mètres")