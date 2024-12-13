lista = ["eh...", "hola", "no", "se", "que", "escribir", "aqui", "entonces", "yo", "escribo", "eso"]

def elementospares():
    for index in enumerate(lista):
        print(index[1])
        if index[0] % 2 != 0:
            print(index[1])

elementospares()