#1
def convertor(grams):
    ounces = 28.3495231 * grams
    return ounces

a = float(input("Write grams: "))
print(convertor(a))


#2
def convertor(F):
    C = (5 / 9) * (F - 32)
    return C
    
a = float(input("Write Fahrenheits: "))
print(convertor(a))



#3
def solve(numheads, numlegs):
    c = -numlegs/2 + 2*numheads
    r = numheads - c
    print("Rabbits:", int(r))
    print("Chickens", int(c))

solve(35, 94)
    

#4
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


#5

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

#6
def rever(sentence):
    ret = ""
    complited = list(sentence.split(" "))
    complited.reverse()
    for i in complited:
        ret+=i
        ret+=" "
    return ret

a = str(input("Write sentence: "))
print(rever(a))

#7

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


#8
def spy_game(nums):
    w = True
    state = 0
    for i in range(0, len(nums)):
        if nums[i] == 0 and state == 0:
            state+=1
        if nums[i] == 0 and state == 1:
            state+=1
        if nums[i] == 7 and state == 2:
            print(True)
            w = False
    if w:
        print(False)
        
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])

#9

def sphere_volume(r):
    v = 4/3 * 3.141592653589793 * r**3
    return v
    
r = float(input("Write radius: "))
print(sphere_volume(r))

#10

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

#11
def pol(string):
    if string == string[::-1]:
        return True
    else:
        return False

string = str(input("Write string: "))
print(pol(string))


#12
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


#13
import random
name = str(input("Hello! What is your name?\n"))
print("\n")
num = random.randint(1, 20)
print("Well, " + name + ", I am thinking of a number between 1 and 20.")
guess = int(input("Take a guess.\n"))
print("\n")
final = True
at = 1
while final:
    if guess == num:
        print("Good job, KBTU! You guessed my number in", at, " guesses!")
        final = False
    
    if guess < num:
        print("Your guess is too low.")
        guess = int(input("Take a guess.\n"))
        print("\n")

        at+=1
        
    if guess > num:
        print("Your guess is too large.")
        guess = int(input("Take a guess.\n"))
        print("\n")

        at+=1




