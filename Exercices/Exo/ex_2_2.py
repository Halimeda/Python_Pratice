from random import choice

def create_sentence(words):
    message = ""
    while len(words) > 0:
        word = choice(words)
        message = message + " " + word
        words.remove(word)

    return message  

words_1 = ['disorder', 'enemy', 'humanity', 'is', 'of', 'the', 'true']
words_2 = ["for", "high", "let's", "new", "score", "shoot", "the"]

print(create_sentence(words_1))
print(create_sentence(words_2))