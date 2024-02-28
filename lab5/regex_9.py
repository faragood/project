import re

with open('row.txt', 'r') as file:
    string1 = file.read()
    lines = string1.split('\n')
    
for string in lines:
    new_string = ""
    for i in range(len(string) - 1):
        if string[i] != ' ' and ((string[i + 1] >= 'A' and string[i + 1] <= 'Z') or (string[i + 1] >= 'А' and string[i + 1] <= 'Я')):
            new_string += (string[i] + ' ')
        else:
            new_string += string[i]
    new_string += string[len(string) - 1]
    print(new_string)
