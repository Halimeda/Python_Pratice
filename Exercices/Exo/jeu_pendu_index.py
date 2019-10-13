from random import randint
word_list = ["coucou", "chat", "porte", "thé", "tasse"]
choose_word = word_list[randint(0, (len(word_list)-1))]
character = []
try_count = 5

print("Le mot choisit contient " + str(len(choose_word)) + " lettres.")
result = ["_ " * len(choose_word)]
print(result)

while ((choose_word != result) and try_count > 0):
    c = input("Choisi une lettre : ")
    character.append(c)
    for i in range(len(word_list) - 1):
        if choose_word[i] in character:
            result[i] = choose_word[i]
        else:
            result[i] = "_ "
    if not character[-1] in choose_word:    
        try_count -= 1
        print("Il te reste " + str(try_count) + " erreurs")
    print("Tu as déjà proposé les lettres suivantes : " + str(character))
    print(result)
    if(choose_word == result):
        print("Felicitation, tu as gagné")
    elif (try_count == 0):
        print("Perdu ! Le mot était : " + choose_word + ". Essaye encore !")