edades = []
def mostrarmayoresque():
    tupla = 1, 22, 23, 4, 18
    for edad in tupla:
        if edad >= 18:
            edades.append("La persona con {} años es mayor de edad".format(edad))
    if edades == []:
        print("Ninguna de las personas de la lista es mayor de edad")

mostrarmayoresque()
for resultado in edades:
    print(resultado)