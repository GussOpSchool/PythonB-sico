def repetir():
    repetido = letra * int(veces)
    return repetido

letra = input("Deme una letra que quieras repetir: ")
veces = input("Cuantas veces quieres repetirla?: ")

repetido = repetir()
print("Aquí está la nueva cadena: {}".format(repetido))