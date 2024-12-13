### IMPORTANTE ###
# Intenta el codigo sacando el '#' de la lista que quieres eligir!
lista = []
#lista = [1, 20, 32, 43, 59, 63, 71]
#lista = [932, 2, 4949, 0, 34]
#lista = [9, 8, 7, 6, 5, 4, 3]


def estaordenado():

    ascendente = sorted(lista)
    print(list(reversed(ascendente)))

    if lista == ascendente:
        print("La lista de numeros '{}' esta en orden ascendente!".format(lista))
    elif lista == list(reversed(ascendente)):
        print("La lista de numeros '{}' esta en orden descendente!".format(lista))
    else:
        print("La lista de numeros '{}' no esta ordenada!".format(lista))

estaordenado()