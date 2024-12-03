cadena = input("Escribe algo y te dire cuantas mayusculas hay: ")
mayusculas = 0

for letra in cadena:
    if letra.isupper():
        mayusculas += 1

print("Tu cadena tiene {} letras mayusculas".format(mayusculas))