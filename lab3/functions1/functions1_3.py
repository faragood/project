def solve(numheads, numlegs):
    c = -numlegs/2 + 2*numheads
    r = numheads - c
    print("Rabbits:", int(r))
    print("Chickens", int(c))

solve(35, 94)
