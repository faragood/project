def filter(numbers_list):
    filtered_list = []
    for i in numbers_list:
        if i == 1:
            continue
            
        error = False
        for d in range(2, i):
            if (i+d)%d == 0:
                error = True
                break
                
        if error == False:
            filtered_list.append(i)
    return filtered_list

aa = str(input("Write list of numbers: "))
aaa = aa.split(" ")
a = []
for i in aaa:
    a.append(int(i))
print(filter(a))
