while True:
    nuevonumero = ""
    numero = input("Dime un numero y te dire solo los digitos pares de el: ")
    for digito in enumerate(numero, start = 1):
        if digito[0] % 2 == 0:
            nuevonumero += digito[1]
    print("Tu nuevo numero es '{}'".format(nuevonumero))