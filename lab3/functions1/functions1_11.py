def pol(string):
    if string == string[::-1]:
        return True
    else:
        return False

string = str(input("Write string: "))
print(pol(string))

