import math
n = float(input("Input number of sides: "))
a = float(input("Input the length of a side: "))
alpha = 2 * math.pi / n
S = 0.5 * math.sin(alpha) * (math.sin((math.pi - alpha)/2) * a / math.sin(alpha))**2 * n
print("The area of the polygon is:", round(S))
