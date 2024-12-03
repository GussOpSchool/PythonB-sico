lista = []
def filtrarpalabras():
    listafiltro = []
    print(minimo)
    for palabra in lista[1:]:
        print(palabra)
        if len(palabra) >= minimo:
            listafiltro.append(palabra)
    return listafiltro

cuantos = int(input("CUANTAS (no cuales) palabras quieres comparar?: "))
for elemento in range(cuantos):
    numeroenlista = input("Dame una palabra: ")
    lista.append(numeroenlista)
minimo = int(input("Cual es el minimo de caracteres que debe tener la palabra para ser considerada?: "))
listafiltro = filtrarpalabras()
print("Las palabras que tienen {} o mas caracteres son:\n{}".format(minimo, listafiltro))