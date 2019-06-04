from random import randint

#Tirage au sort thématique Game Jam

#thematics = ["cyberpunk", "yeux", "sang", "Utopie", "food", "ice", "peste noire", "phobia", "mirror", "girls and sword"]
#print(thematics[randint(0, (len(thematics) - 1))])

#Tirage au sort participant et formation équipe

code = ["Aurélie", "Shéra", "Hélène", "Alex"]
dessin = ["Ariane", "Yavanah", "Aurore", "Jess'"]
middle = ["Rumy", "Yiwei", "Farah", "Tugba"]

while((len(code) > 0) and (len(dessin) > 0) and (len(middle) > 0)):
    i = randint(0, (len(code) - 1))
    j = randint(0, (len(dessin) - 1))
    k = randint(0, (len(middle) - 1))
    print(code[i], " + ", dessin[j], " + ", middle[k], "\n")
    code.remove(code[i])
    dessin.remove(dessin[j])
    middle.remove(middle[k])

if(len(code) > 0):
    for index in range(len(code)):
        print (code[index])

elif(len(dessin) > 0):
        for index in range(len(dessin)):
            print (dessin[index])

elif(len(middle) > 0):
        for index in range(len(middle)):
            print (middle[index])
