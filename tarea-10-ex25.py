lista = []
def grandelista():
    tempmayor = 0
    for numero in lista[1:]:
        if numero > tempmayor:
            tempmayor = numero
        return tempmayor

cuantos = int(input("CUANTOS (no cuales) numeros quieres comparar?: "))
for elemento in range(cuantos):
    numeroenlista = int(input("Dame el numero: "))
    lista.append(numeroenlista)
mayor = grandelista()
print("El mayor numero de esta lista:\n{}\nes {}".format(lista, mayor))