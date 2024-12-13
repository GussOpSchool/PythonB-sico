primos = 0
listaprimos = []
for numero in range(1, 101):
    esprimo = True

    for cadanumero in range(2, numero):
        if numero % cadanumero == 0:
            esprimo = False
            break  
    if esprimo:
        primos += 1
        if numero < 10:
            listaprimos.append("0" + str(numero))
        else:
            listaprimos.append(numero)

fila = []
segundafila = False

print("Aqui una tabla para todos los numeros primos del 1 al 100:\n\n")

for elementoeindex in listaprimos:
    fila.append(str(elementoeindex))
    if len(fila) == 13:
        print(".", end = "")
        print("__." * 13)
        print("|", end = "")
        print("|".join(fila), end = "|\n")
        print("̇ ", end = "") if segundafila else None
        print("̇‾‾̇̇̇ " * 13) if segundafila else None
        fila = []
        segundafila = True

print("\n\nDe los numero 1 al 100, {} son primos".format(primos))
