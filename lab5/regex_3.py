import re
file = open('row.txt', 'r')
string = file.read()
list = list(string.split('\n'))
for i in range(len(list)-1):
    x = re.search(".*_[a-z].*|.*[a-z]_.*", list[i])
    if x:
        print("In " + str(i+1) + "th string: " + x.group())

