def mayordeedad():
    edad = int(input("Dime tu edad: "))

    if edad == 18:
        print("Tienes justo 18 años")
    elif edad < 18:
        print("Eres menor de edad")
    elif edad > 18:
        print("Eres mayor de edad")
