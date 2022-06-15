str = input('Enter the sentence :\n')
sentence = dict()
words = str.split()
for word in words:
    if word in sentence:
        sentence[word]+=1
    else:
        sentence[word] = 1
print (sentence)

