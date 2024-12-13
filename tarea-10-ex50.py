lista = [1, 2, 3, 4, 5, 7, 4]

def eliminaduplicados():

    global lista

    if len(lista) != len(set(lista)):
        lista = set(lista)
        print("Tu lista tenia elementos duplicados, aqui la lista actualizadda:\n{}".format(lista))
    else:
        print("La lista NO tiene elementos duplicados, ningun cambio hecho:\n{}".format(lista))

eliminaduplicados()