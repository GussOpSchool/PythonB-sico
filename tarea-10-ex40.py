def cuadrados():
    
    global numero

    for e in range(4):
        print("{} elevado a 2 es {}".format(numero, numero ** 2))
        numero -= 4


while True:
    numero = int(input("Pon un numero menor que 100 y hare algo muy random: "))

    if numero > 100 or numero <= 0:
        print("Por favor introduce un numero positivo entre 1 y 100")
    else:
        break

cuadrados()

