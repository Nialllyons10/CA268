import sys

list = sys.argv[1:]
string_one = ''
num = 0

for i in list: 
    string_one = string_one + list[num] + ':'
    num += 1

print(':' + string_one)
