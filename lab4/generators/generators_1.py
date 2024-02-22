def generator(n):
    for i in range(1, int(n**(1/2))+1):
        yield i**2
n = int(input("Write n: "))
print(list(generator(n)))
