
#1
class GetString():
    def __init__(self):
        self.stringtoprint = ""
        
    def getstring(self):
        self.stringtoprint = input()
        
    def uppercase(self):
        print(self.stringtoprint.upper())

stri = GetString()
stri.getstring()
stri.uppercase()

#2

class Shape():
    def __init__(self):
        pass
    def area(self):
        return "0"
class Square(Shape):
    def __init__(self):
        super().__init__()
        self.a = float(0)
        
    def length(self):
        self.a = float(input())
        
    def area(self):
        return self.a**2
        
shapearea = Shape()
squarearea = Square()

print("Area of shape:", shapearea.area())

squarearea.length()
print("Area of square:", squarearea.area())

#3
class Shape():
    def __init__(self):
        pass
    def area(self):
        return "0"

class Rectangle(Shape):
    def __init__(self, length_init, width_init):
        super().__init__()
        self.length = length_init
        self.width = width_init
    
    def area(self):
        print("Area:", self.length * self.width)

length = float(input("Write lenght: "))
width = float(input("Write width: "))
rectangle_area = Rectangle(length, width)
rectangle_area.area()


#4
class Points():
    def __init__(self, x1, y1, x2, y2):
        self.x1c = int(x1)
        self.y1c = int(y1)
        self.x2c = int(x2)
        self.y2c = int(y2)
    
    def show(self):
        print("coordinates of the 1st point:", self.x1c, self.y1c)
        print("coordinates of the 2st point:", self.x2c, self.y2c)
    
    def move(self):
        self.x1c = int(input("Write x for first point:"))
        self.y1c = int(input("Write y for first point:"))
        self.x2c = int(input("Write x for second point:"))
        self.y2c = int(input("Write y for second point:"))
        
    def dist(self):
        distace = ((self.x1c - self.x2c)**2 + (self.y1c - self.y2c)**2)**(1/2)
        print("Distance between fist and second points:", distace)
coordinates = Points(0, 0, 0, 0)
coordinates.show()
coordinates.move()
coordinates.show()
coordinates.dist()


#5
class Bank():
    def __init__(self, owner_s, balance_s):
        self.owner = owner_s
        self.balance = float(balance_s)
    
    def show_balance(self):
        print("Your balance is:", self.balance)
        
    def deposit(self, sum_of_deposit):
        self.balance+=sum_of_deposit
        
    def withdraw(self, sum_of_withdraw):
        if sum_of_withdraw > self.balance:
            print("Withdraw is greater than balance!")
        else:
            self.balance-=sum_of_withdraw

account = Bank("Farid", 0)
action = True
while action:
    account.show_balance()
    choice = int(input("Print 1 to choose deposit, 2 to choose withdraw or 0 to quite: "))
    if choice == 0:
        action = False
    if choice == 1:
        sum_for_deposit = float(input("Write sum of deposit: "))
        account.deposit(sum_for_deposit)
    if choice == 2:
        sum_for_withdraw = float(input("Write sum of withdraw: "))
        account.withdraw(sum_for_withdraw)


#6
def filter_prime(number):
    if number == 1:
        return False
    for d in range(2, number):
        if (number+d)%d == 0:
            return False
    return True
        
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list(filter(lambda s: filter_prime(s), a)))



    
