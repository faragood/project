def generator(n):
    for i in range(0, int(n/2) + 1):
        yield 2*i
n = int(input("Write n: "))
print(list(generator(n)))
