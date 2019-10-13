from random import choice
words = ['disorder', 'enemy', 'humanity', 'is', 'of', 'the', 'true']
message = ""

while len(words) > 0:
    word = choice(words)
    message = message + " " + word
    words.remove(word)

print(message)