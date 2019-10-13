# 1 - Préparation
#   Choisir le mot à faire deviner
#   Préparer les variables nécessaires
mot_a_deviner = "python"
lettres_proposees = []
result = ["-" * len(mot_a_deviner)]

while result != list(mot_a_deviner):

    # 2 - Demander une lettre
    lettre = input("Proposez une lettre : ")
    lettres_proposees.append(lettre)

    # 3 - Vérifier si la lettre est dans le mot
    #       - afficher le mot avec des "-"
    if lettre in mot_a_deviner:
        print("La lettre est dans le mot!")
    else:
        print("La lettre n'est pas dans le mot :(")

    # Afficher le mot avec des "-" pour les lettres non trouvées
    
    # Version avec le while :
    # index = 0
    # while index < len(mot_a_deviner):
    #     if mot_a_deviner[index] in lettres_proposees:
    #         result[index] = mot_a_deviner[index]
    #     else:
    #         result[index] = "-"

    #     index = index + 1

    for index in range(len(mot_a_deviner)):
        if mot_a_deviner[index] in lettres_proposees:
            result[index] = mot_a_deviner[index]
        else:
            result[index] = "-"

    print(result)


# 4 - Répéter 2 & 3 tant qu'on a pas deviné le mot entier


