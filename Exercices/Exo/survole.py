from random import randint
from random import choice

def create_sentence(words):

    sentence_list = ""
    while len(words) > 0:
        index = len(words) - 1
        i = randint(0, index)
        sentence_list = sentence_list + " " + words[i]
        del words[i]
    return(sentence_list)

words1 = ["disorder", "enemy", "humanity", "is", "of", "the", "true"]
words2 = ["for", "high", "let's", "new", "score", "shoot", "the"]
wich_list = [words1, words2]

#print(create_sentence(words1))
#print(create_sentence(words2))

sentence = choice(wich_list)
print(create_sentence(sentence))