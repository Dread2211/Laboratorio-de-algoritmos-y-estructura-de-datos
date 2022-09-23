palabra = input('ingresa una palabra: ')

def lado():
    print("*", end="")
    for i in range(len(palabra)):
        print("*", end="")
    print("*")

lado()
print("*" + palabra + "*")
lado()
