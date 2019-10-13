word = input("Enter a word : ")
word_list = []
while word != "end":
    word_list.insert (0, word)
    word = input("Enter a word : ")
for i in word_list:
    print(i)