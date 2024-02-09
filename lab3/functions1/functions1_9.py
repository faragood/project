def sphere_volume(r):
    v = 4/3 * 3.141592653589793 * r**3
    return v
    
r = float(input("Write radius: "))
print(sphere_volume(r))

