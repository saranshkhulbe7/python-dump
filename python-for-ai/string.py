sentence = "Hi there this is shaka lala boom boom"

words = []
word = ""
length = len(sentence)
for i in range(0, length):
    letter = sentence[i]
    if letter != " ":
        word += letter
    else:
        words.append(word)
        word = ""

if(word != ""):
    words.append(word)

print(words)