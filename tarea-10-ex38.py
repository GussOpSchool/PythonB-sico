def rima():

    print("Puedo decir si dos palabras riman:")
    palabra1 = input("Escribe la primera palabra: ")
    palabra2 = input("Y la segunda: ")
    if palabra1[-1 : -4 : -1] == palabra2[-1 : -4 : -1]:
        print("Las palabras '{}' y '{}' riman!".format(palabra1, palabra2))
    elif palabra1[-1 : -3 : -1] == palabra2[-1 : -3: -1]:
        print("Las palabras '{}' y '{}' pueden rimar".format(palabra1, palabra2))
    else:
        print("Las palabras '{}' y '{}' NO riman...".format(palabra1, palabra2))

rima()