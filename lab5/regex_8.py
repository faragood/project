import re
file = open('row.txt', 'r')
string = file.read()
list = list(string.split('\n'))
pattern = re.compile(r'[A-ZА-Я][^ [A-ZА-Я]*]*|^[A-ZА-Я][^ ]*')
for i in list:
    x = pattern.findall(i)
    print(x)
