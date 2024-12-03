# FUNCIONES y VARIABLES #

binario = False
octal = False
dec = False
hexadec = False

def resetearbases():
    global binario, octal, dec, hexadec
    binario = False
    octal = False
    dec = False
    hexadec = False

resetearbases()

def base():
    global binario, octal, dec, hexadec
    resetearbases()
    print("\n Elige por que base quieres trabajar:")
    print("1. Binario")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")
    print("5. Salir")
    base = int(input("Elige con un numero: "))
    match(base):
        case 1:
            binario = True
        case 2:
            octal = True
        case 3:
            dec = True
        case 4:
            hexadec = True
        case 5:
            salir()
        case _:
            print("¡Opcion invalida!")

def suma():
 
    if hexadec:
        X = int(input("Deme el primer numero: "), 16)
        Y = int(input("Y el segundo: "), 16)
    else:
        X = int(input("Deme el primer numero: "))
        Y = int(input("Y el segundo: "))
    
    if binario:
        resultado = bin(X + Y)
    elif octal:
        resultado = oct(X + Y)
    elif dec:
        resultado = X + Y
    elif hexadec:
        resultado = hex(X + Y)

    if binario:
        print("{} + {} = {}".format(bin(X)[2:], bin(Y)[2:], resultado[2:]))
    elif octal:
        print("{} + {} = {}".format(oct(X)[2:], oct(Y)[2:], resultado[2:]))
    elif dec:
        print("{} + {} = {}".format(X, Y, resultado[2:]))
    elif hexadec:
        print("{} + {} = {}".format(hex(X)[2:], hex(Y)[2:], resultado[2:]))

def resta():

    if hexadec:
        X = int(input("Deme el primer numero: "), 16)
        Y = int(input("Y el segundo: "), 16)
    else:
        X = int(input("Deme el primer numero: "))
        Y = int(input("Y el segundo: "))
    
    if binario:
        resultado = bin(X - Y)
    elif octal:
        resultado = oct(X - Y)
    elif dec:
        resultado = X - Y
    elif hexadec:
        resultado = hex(X - Y)

    if binario:
        print("{} - {} = {}".format(bin(X)[2:], bin(Y)[2:], resultado[2:]))
    elif octal:
        print("{} - {} = {}".format(oct(X)[2:], oct(Y)[2:], resultado[2:]))
    elif dec:
        print("{} - {} = {}".format(X, Y, resultado[2:]))
    elif hexadec:
        print("{} - {} = {}".format(hex(X)[2:], hex(Y)[2:], resultado[2:]))

def multi():

    if hexadec:
        X = int(input("Deme el primer numero: "), 16)
        Y = int(input("Y el segundo: "), 16)
    else:
        X = int(input("Deme el primer numero: "))
        Y = int(input("Y el segundo: "))
    
    if binario:
        resultado = bin(X * Y)
    elif octal:
        resultado = oct(X * Y)
    elif dec:
        resultado = X * Y
    elif hexadec:
        resultado = hex(X * Y)

    if binario:
        print("{} * {} = {}".format(bin(X)[2:], bin(Y)[2:], resultado[2:]))
    elif octal:
        print("{} * {} = {}".format(oct(X)[2:], oct(Y)[2:], resultado[2:]))
    elif dec:
        print("{} * {} = {}".format(X, Y, resultado[2:]))
    elif hexadec:
        print("{} * {} = {}".format(hex(X)[2:], hex(Y)[2:], resultado[2:]))

def divis():

    if hexadec:
        X = int(input("Deme el primer numero: "), 16)
        Y = int(input("Y el segundo: "), 16)
    else:
        X = int(input("Deme el primer numero: "))
        Y = int(input("Y el segundo: "))

    if binario:
        resultado = bin(X / Y)
    elif octal:
        resultado = oct(X / Y)
    elif dec:
        resultado = float(X / Y)
    elif hexadec:
        resultado = hex(X / Y)

    if binario:
        print("{} / {} = {}".format(bin(X)[2:], bin(Y)[2:], resultado[2:]))
    elif octal:
        print("{} / {} = {}".format(oct(X)[2:], oct(Y)[2:], resultado[2:]))
    elif dec:
        print("{} / {} = {}".format(X, Y, resultado[2:]))
    elif hexadec:
        print("{} / {} = {}".format(hex(X)[2:], hex(Y)[2:], resultado[2:]))

def salir():
    confirmar = input("¿Seguro que quieres salir? (y/n): ")
    if confirmar == "y" or "Y":
        exit()

def menu():
    print(" ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    print(" ")
    respuesta = int(input("Elige la operacion con un numero: "))
    
    match (respuesta):
            case 1:
                suma()

            case 2:
                resta()
                
            case 3:
                multi()
                
            case 4:
                divis()
                
            case 5:
                salir()
            case _:
                print("¡Opcion invalida!")


###### PROGRAMA ######
while True:
    base()
    menu()