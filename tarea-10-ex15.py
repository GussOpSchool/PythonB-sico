def grande_de_tres():
    tempmayor = check_numero(num1, num2)   
    mayor = check_numero(tempmayor, num3)
    return mayor

def check_numero(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2
    
print("Voy a coger 3 numeros y decir cual es el mayor de ellos")
num1 = int(input("Deme el primer numero: "))
num2 = int(input("Deme el segundo numero: "))
num3 = int(input("Deme el tercer numero: "))
mayor = grande_de_tres()
print("El mayor numero entre '{}, {} y {}' es {}".format(num1, num2, num3, mayor))