cuantos = 0
volver = False
for cuantosasteriscos in range(5):
    if cuantos == 3:
        volver = True
    if not volver:
        cuantos += 1
    else:
        cuantos -= 1
    print("*" * cuantos)