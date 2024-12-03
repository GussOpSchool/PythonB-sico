### FUNCIONES Y VARIABLES ###
tabla = []
def preguntar():
    ano = input("En que ano estamos?: ")
    cuantas = int(input("Cuantas personas quieres guardar el cumpleanos? Dame un numero entero: "))
    for cadapersona in range(cuantas):
        persona = input("\nCual es el nombre de la persona?: ")
        cumple = input("Cual es el ano de su nacimiento?: ")
        hara = input("Cuantos anos cuimplira? (No cuantos tiene, pero cuanto hara): ")
        tabla.append("{:<15}{:<20}{:<10}\n".format(persona, cumple, hara))
    return ano

### PROGRAMA ###

ano = preguntar()
print("\n\nAqui tienes tu tabla de cumpleanos:\n")
print("Ano actual: {},\n{:<15}{:<20}{:<10}".format(ano, "Nombre", "Fecha de Nacimiento", "Cuantos anos hara"))
print("".join(tabla))
