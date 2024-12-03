a = "Hola"
b = input("Escribe una palabra: ")
 
# mostrar caracter por caracter

for c in b:
    print(c) 

# longitud palabra

print(len(b))

# comparar si las palabras son iguales

if a == b:
    print(a + " y " + b + " son iguales")
else:
    print(a + " y " + b + " no son iguales")
# Juntarlo por guiones

print(a + "-" + b)

# repetir b tres veces

print(b * 3)

# vocal "a" esta?

if "a" or "A" in b:
    print("Hay una a en la palabra " + b)
else:
    print("No hay una a en la palabra " + b)