def pedircosas():
    
    global capitalistainicial, intereses, anos

    while True:
        try:
            capitalistainicial = int(input("Introduce una cantidad de dinero entre 50000 y 800000 euros: "))
            if capitalistainicial >= 50000 and capitalistainicial <= 800000:
                break
            else:
                print("\nPor favor elige un valor entre 50000 y 800000\n")
        except:
            print("\nIntroduce un numero valido\n")
    
    while True:
        try:
            intereses = int(input("Introduce (sin porcentajes) el interes que quieres evaluar. Acuerdate que el minimo es 0.5% y el maximo es 13%: "))
            if intereses >= 0.5 and intereses <= 13:
                break
            else:
                print("Por favor elige un numero entre 0.5 y 13")
        except:
            print("\nIntroduce un numero valido (acuerdate de no poner el simbolo '%' y usar puntos si no es un numero exacto)\n")

    while True:
        try:
            anos = int(input("Por cuantos anos pretendes dejar tus capitales crecer? (minimo 3 anos, maximo 40 anos): "))
            if anos >= 3 and anos <= 40:
                break
            else:
                print("Por favor elige un ano entre 3 y 40")
        except:
            print("\nIntroduce un ano valido\n")

def capitalista():
    capitalistafinal = capitalistainicial * (1 + intereses / 100) ** anos
    print("Tu capital final es", round(capitalistafinal, 2))

# PROGRAMA #
siono = "s"
print("\n")
print("Puedo contar cuanto se convertira tus capitales basados en el año y porcentajes promedios")

while siono == "s":
    pedircosas()
    capitalista()
    siono = input("Quieres intentar con otros valores? (S/n): ").lower()