
def verlistar():
    lista = []
    iten = ""
    while True:
        iten = input("Anade un iten a la lista. Escribe '.' para terminar: ")
        if iten == ".":
            break
        lista.append(iten)
    return lista

def verfrase():
    frase = input("Escribe una frase para contar las letras: ")
    return frase

print(" ")
print("Elige de que quieres que cuente la longitud:")
print("1. Lista")
print("2. Frase")
respuesta = input("Elige con un numero: ")

match(respuesta):
    case "1":
        lista = verlistar()
        verificar = len(lista)
        print("\nTu lista tiene {} elementos:".format(verificar))
        for iten in lista:
            print(iten)
    case "2":
        frase = verfrase()
        verificar = len(frase)
        print("\nTu frase tiene {} letras (contando los espacios):".format(verificar))
        print(frase)
