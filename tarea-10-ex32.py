nombres = ["Alejandro", "Gustavo", "Joan", "ana", "Carlos"]
empiezaa = []

def comienzapor():
    for nombre in nombres:
        letranombre = nombre[0]
        if letranombre.upper() == "A":
            empiezaa.append(nombre)
    if empiezaa == []:
        print("Ninguno de los nombres empieza por 'A'")

comienzapor()

if empiezaa != []:
    print("\nLos nombres que empiezan por 'A' son:")
    for nombre in empiezaa:
        print(nombre)
