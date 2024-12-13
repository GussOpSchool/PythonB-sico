listapalabras = ["platano", "manzana", "uva", "sandia", "aguacate", "guayaba"]

def indexpalabra():
    for fruta in enumerate(listapalabras):
        indexfruta = fruta[0] + 1, fruta[1]
        print(indexfruta)

print("\nAquí el index de cada una de las palabras de la lista:\n")
indexpalabra()