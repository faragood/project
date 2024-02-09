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

