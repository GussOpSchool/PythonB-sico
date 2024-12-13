import random

def lista20elementos():
    print("Voy a crear una lista de 20 elementos aleatorios...")
    lista = []
    for elemento in range(20):
        elemento = random.randint(1, 100)
        lista.append(elemento)
    print("La lista generada con numeros de 1 a 100 es:\n{}".format(lista))

lista20elementos()