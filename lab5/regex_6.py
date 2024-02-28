import re
file = open('row.txt', 'r')
string = file.read()
new_string = ""
for i in range(len(string)):
    if string[i] == ' ' or string[i] == ',' or string[i] == '.':
        new_string+=":"
    else:
        new_string+=string[i]
print(new_string)
