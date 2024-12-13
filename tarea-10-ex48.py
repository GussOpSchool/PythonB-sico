lista = [1, 2, 3, 4, 5, 7, 3]

def hayduplicados():
    if len(lista) != len(set(lista)):
        print("La lista tiene elementos duplicados")
    else:
        print("La lista NO tiene elementos duplicados")

hayduplicados()