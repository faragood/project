import re
file = open('row.txt', 'r')
string = file.read()
list = list(string.split('\n'))
for i in range(len(list)-1):
    x = re.search(".*abb.*|.*abbb.*", list[i])
    if x:
        print("In " + str(i+1) + "th string: " + x.group())

