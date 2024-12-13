while True:
    numero = input("Dime un numero y te dire si la suma de los digitos es par o impar: ")
    if len(numero) % 2 == 0:
        print("La suma de los digitos de '{}' es par ({})".format(numero, len(numero)))
    else:
        print("La suma de los digitos de '{}' NO es par ({})".format(numero, len(numero)))