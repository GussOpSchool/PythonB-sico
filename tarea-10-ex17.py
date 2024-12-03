caracter = input("Deme un caracter y te dire si es una vocal o consonante. Escribe solo UNA letra: ")
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
if caracter in vocales:
    print("La letra {} es una vocal".format(caracter))
else:
    print("La letra {} es una consonante".format(caracter))