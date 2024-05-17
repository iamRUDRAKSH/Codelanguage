#Get input form user
#Ask if they want to code or decode
#To code :
# if word contains more than 2 letters remove first letter and append it to the end and then add three random letters at the end and start 
# of the word
# else reverse the word
#To decode :
# if word contains less than 3 words reverse it
# or if it contains more than 3 words
# remove first and last three letters of the word and then move last letter of the word to first position

import random
import string

strin = input("Enter your sentence : ")
words = strin.split()
nwords = []
letters = string.ascii_lowercase
ans = input("Code or Decode : ")
if ans == "code" or ans == "Code":
    for word in words:
        if len(word) > 2:
            r1 = ''.join(random.choice(letters) for _ in range(3))
            r2 = ''.join(random.choice(letters) for _ in range(3))
            nword = r1 + word[1:] + word[0] + r2
        else:
            nword = word[::-1]
        nwords.append(nword)    
    print(" ".join(nwords))        
elif ans == "decode" or ans == "Decode":
    for word in words:
        if len(word) <= 2:
            nword = word[::-1]
        else:
            nword = word[3:-3]
            nword = nword[-1] + nword[:-1]
        nwords.append(nword)    
    print(" ".join(nwords))      
else:
    print("Invalid input!!\n")