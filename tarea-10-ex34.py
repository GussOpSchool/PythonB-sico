nombres = ["Alejandro", "Gustavo", "Joan", "ana", "Carlos"]
empieza = []
letra = input("Cual es la primera letra del nombre que quieres: ").upper()

def comienzapor():
    for nombre in nombres:
        letranombre = nombre[0]
        if letranombre.upper() == letra:
            empieza.append(nombre)
    if empieza == []:
        print("Ninguno de los nombres empieza por '{}'".format(letra))

comienzapor()

if empieza != []:
    print("\nLos nombres que empiezan por '{}' son:".format(letra))
    for nombre in empieza:
        print(nombre)
