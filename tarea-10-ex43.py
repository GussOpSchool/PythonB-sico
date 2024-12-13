while True:
    numero = int(input("Deme un numero y te doy la tabla de multiplicaciones: "))
    if 1 <= numero <= 20:
        break
    else:
        print("Introduce un numero entre 1 y 20")
print("")
for tabla in range(11):
    print("{} * {} = {}".format(numero, tabla, numero * tabla))