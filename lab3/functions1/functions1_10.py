def uni(num):
    x = []
    for i in num:
        if i not in x:
            x.append(i)
    return x

aa = str(input("Write list of numbers: "))
aaa = aa.split(" ")
a = []
for i in aaa:
    a.append(int(i))
print(uni(a))

