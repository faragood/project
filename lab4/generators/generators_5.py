def reverse(n):
     i = n
     while i >= 0:
        yield i
        i-=1
n = int(input("Input n: "))
print(list(reverse(n)))
