lista = []
def palabramaslarga():
    tempmayor = 0
    for palabra in lista[1:]:
        if len(palabra) > tempmayor:
            tempmayor = palabra
        return tempmayor

cuantos = int(input("CUANTAS (no cuales) palabras quieres comparar?: "))
for elemento in range(cuantos):
    numeroenlista = input("Dame una palabra: ")
    lista.append(numeroenlista)
mayor = palabramaslarga()
print("La mayor palabra de esta lista:\n{}\nes '{}'".format(lista, mayor))