lista1 = [1, 2, 4, 8, 5, 6]
lista2 = [0, 1, 2, 3, 4, 5, 6]

encomun = str(set(lista1) & set(lista2))

def superposicion():
    if encomun != "set()":
        haycomun = True
    else:
        haycomun = False
    if haycomun == False:
        print("Ningun elemento se repite en las listas:\n")
        print(lista1)
        print(lista2)
    else:
        print("Hay elementos que se repiten en las listas:\n")
        print(lista1)
        print(lista2)

superposicion()