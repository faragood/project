def histogram(a):
    for i in a:
        output = ""
        for j in range(i):
            output+="*"
        print(output)
aa = str(input("Write list of numbers: "))
aaa = aa.split(" ")
a = []
for i in aaa:
    a.append(int(i))
histogram(a)

