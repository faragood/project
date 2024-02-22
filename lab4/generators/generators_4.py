import math
def squares(a, b):
    for i in range(math.ceil(a**(1/2)) , int(b**(1/2)) + 1):
        yield i**2
a = int(input("Input a: "))
b = int(input("Input b: "))
print(list(squares(a,b)))
