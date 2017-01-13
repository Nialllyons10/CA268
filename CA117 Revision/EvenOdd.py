import sys

word = sys.argv[1]
word_len = len(word)

num_div = word_len // 2

if word_len % 2 == 0: 
    print(word[num_div:])
else: 
    print(word[0] + word[-1])
