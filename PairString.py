 import sys
 
word = sys.argv[1]
i = 0
length = len(word)
     
for character in word:
  if i + 1 < length:
    print(character + word[i+1])
     i += 
  else:
    pass
