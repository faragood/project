def generator3(n):
    for i in range(1, int(n/3) + 1):
        yield i*3
def generator4(n):
    for i in range(1, int(n/4) + 1):
        yield i*4
n = int(input("Input n: "))
print("List of numbers divisible by 3:", *list(generator3(n)))
print("List of numbers divisible by 4:", *list(generator4(n)))
