from itertools import permutations

def permuta(stri):
    permut = list(permutations(stri))
    for i in permut:
        x = ""
        for j in i:
            x += j
        print(x)

stri = str(input("Write string: "))
permuta(stri)

