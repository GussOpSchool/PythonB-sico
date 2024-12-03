# FUNCIONES #
def suma():
 
    X = (input("Deme el primer numero: "))
    Y = (input("Y el segundo: "))

    resultado = float(X) + float(Y)

    print("{} + {} = {}".format(X, Y, resultado))

def resta():

    X = (input("Deme el primer numero: "))
    Y = (input("Y el segundo: "))

    resultado = float(X) - float(Y)

    print("{} - {} = {}".format(X, Y, resultado))

def multi():

    X = (input("Deme el primer numero: "))
    Y = (input("Y el segundo: "))

    resultado = float(X) * float(Y)

    print("{} * {} = {}".format(X, Y, resultado))

def divis():

    X = (input("Deme el primer numero: "))
    Y = (input("Y el segundo: "))

    resultado = float(X) / float(Y)

    print("{} / {} = {}".format(X, Y, resultado))

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
    menu()