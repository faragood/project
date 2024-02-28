import re
file = open('row.txt', 'r')
string = file.read()
new_string = string[0].lower()
for i in range(1, len(string)):
    if string[i] == " " or string[i] == "_":
        continue
    elif string[i-1] == "\n":
        new_string+=string[i].lower()
        continue
    elif string[i-1] == " ":
        new_string+=string[i].upper()
        continue
    elif string[i] != " ":
        new_string+=string[i].lower()
print(new_string)



