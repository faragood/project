def has_33(num):
    w = True
    for i in range(0, len(num)-1):
        if num[i] == 3 and num[i + 1] == 3:
            print(True)
            w = False
    if w:
        print(False)
    
has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])

