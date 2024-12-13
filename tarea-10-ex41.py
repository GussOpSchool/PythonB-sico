while True:
    numero = input("Dime un numero y te dire cuantos digitos tiene (min. 1, max. 900000): ")
    if 1 <= int(numero) <= 900000:
        print("El numero {} tiene {} digitos".format(numero, len(numero)))
    else:
        print("Introduce un numero valido!")