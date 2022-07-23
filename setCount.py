from english_words import *

myLength = len(english_words_lower_alpha_set)

print(myLength)

fiveLetters = 0
wordcount = 0
#allFives = set()
counts = {}
LIMIT = 10

for n in english_words_lower_alpha_set:
    wordcount+=1
    letterCount = len(n)
    mykeys = counts.keys()
    if letterCount >=LIMIT:
        letterCount = str(LIMIT) + "+"
    if letterCount in mykeys:
        counts[letterCount] += 1
    else:
        counts[letterCount] = 1

for wordLength,count in counts.items():
    print("Words of length " + str(wordLength) + " : " + str(count))
    
    #if len(n)== 5:
        #fiveLetters +=1
        #allFives.add(n)
        





