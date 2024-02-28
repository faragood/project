import re
file = open('row.txt', 'r')
string = file.read()
new_string = string[0].lower()
for i in range(0, len(string)-1):
    if string[i] != " " and ((string[i + 1] >= 'A' and string[i + 1] <= 'Z') or (string[i + 1] >= 'А' and string[i + 1] <= 'Я')):
        new_string += (string[i].lower() + '_')
    elif string[i] == ' ':
        new_string += '_'
    else:
        new_string+= string[i].lower()
print(new_string)

