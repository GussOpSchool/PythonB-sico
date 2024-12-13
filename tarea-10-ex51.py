archivo = open("tarea-10-ex51.txt", "r")

def crearlistafichero():
    global palabrasfichero
    palabrasfichero = []
    for parrafo in archivo:
        palabrasfichero.append(parrafo.split(" "))


print("Voy a hacer una lista de las palabras del fichero 'tarea-10-ex51.txt'...")
crearlistafichero()
print("\nAquí esta la lista importada:\n{}".format(palabrasfichero))