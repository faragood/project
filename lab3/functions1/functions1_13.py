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
