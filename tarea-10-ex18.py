lista = ["1", "3", "6", "10", "4"]

def sumarlista():
        suma = 0
        for iten in lista:
            suma += int(iten)
        print("La suma de '{}' es {}".format(lista, suma))

def multilista():
    multi = 1
    for iten in lista:
        multi *= int(iten)
    print("La multiplicacion de '{}' es {}".format(lista, multi))


respuesta = input("\nQuieres sumar (1) o multiplicar(2) la lista: {}?: ".format(lista))

match(respuesta):
    case "1":
        resultado = sumarlista()
    case "2":
        resultado = multilista()
        
