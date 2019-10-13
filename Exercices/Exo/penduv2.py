from random import choice
# 1 - Préparation
#   Choisir le mot à faire deviner
#   Préparer les variables nécessaires
liste_de_mots = ["python", "programme", "print", "exercice", "cours", "anticonstitutionnel", "sublime"]
mot_a_deviner = choice(liste_de_mots)

lettres_proposees = []
result = None

while result != mot_a_deviner:

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
    result = ""
    for c in list(mot_a_deviner):
        if c in lettres_proposees:
            result = result + c
        else:
            result = result + "-"

    print(result)


# 4 - Répéter 2 & 3 tant qu'on a pas deviné le mot entier


