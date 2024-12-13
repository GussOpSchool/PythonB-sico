numero1 = int(input("Deme un numero y sumaré todos los numeros desde el: "))
numero2 = int(input("Hasta el numero: "))

suma = 0
for sumador in range(numero1, numero2 + 1):
    suma += sumador

print("El numero sumado es '{}' (desde el '{}' hasta '{}')".format(suma, numero1, numero2))