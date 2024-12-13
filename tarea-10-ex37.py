import emoji
import time
import random

# Diccionario para los emojis #
emoji = {
    "0": "0️⃣",
    "1": "1️⃣",
    "2": "2️⃣",
    "3": "3️⃣",
    "4": "4️⃣",
    "5": "5️⃣",
    "6": "6️⃣",
    "7": "7️⃣",
    "8": "8️⃣",
    "9": "9️⃣",
    "NO": "❌",
    "CASI": "❔",
    "SI": "✅"
}

# Definiciones, Variables #

intentos = 0
facil = False
medio = False
dificil = False

def pocoapoco(texto, pausa = 0.00):
    for caracter in texto:
        print(caracter, end = '', flush = True)
        time.sleep(pausa)

def tutorial():
    texto = (""" Bienvenido al juego MASTERMIND!
        Para jugar es muy sencillo:
        1. Yo eligire aleatoriamente un numero de 4 digitos
        2. Piensa y introduce cualquier numero (desde que tenga 4 digitos)
        3. Te dare pistas a partir de lo que tengas:
            - Si tienes un '{}', este numero no esta en el codigo
            - Si tienes un '{}', el numero esta en el codigo pero en el lugar equivocado
            - Si tienes un '{}', el numero esta en la posicion correcta
        Dificultades:
        - Facil: Nunca repito numeros. Tienes 8 intentos
        - Medio: A veces repito numeros. Tienes 6 intentos
        - Dificil: Siempre repito numeros. Tienes 4 intentos

    """.format(emoji["NO"], emoji["CASI"], emoji["SI"]))
    pocoapoco(texto)

def opciones():
    global intentos, facil, medio, dificil
    respuesta = input("Elige con una letra (F para facil, M para medio, D para dificil): ").lower()
    match(respuesta):
        case "f":
            intentos = 8
            facil = True
            print("\nJuego en modo facil:")
        case "m":
            intentos = 6
            medio = True
            print("\nJuego en modo medio:")
        case "d":
            intentos = 4
            dificil = True
            print("\nJuego en modo dificil:")

def numerosrepetidos():
        while True:
            codigosecreto = ""
            for veces in range(4):
                digitosecreto = random.randint(0, 9)
                digitosecreto = str(digitosecreto)
                codigosecreto += digitosecreto
            if len(set(codigosecreto)) != 4:
                return codigosecreto

def numerosnorepetidos():
    while True:
        codigosecreto = ""
        for veces in range(4):
            digitosecreto = random.randint(0, 9)
            digitosecreto = str(digitosecreto)
            codigosecreto += digitosecreto
        if len(set(codigosecreto)) == 4:
            return codigosecreto

def corregir(codigosecreto, entrada):
    numero = " ".join([emoji[emojinum] for emojinum in entrada])
    plista = []
    leido = [False] * 4
    
    for posicion in range(4):
        if entrada[posicion] == codigosecreto[posicion]:
            plista.append(emoji["SI"])
            leido[posicion] = True
        else:
            plista.append("REVISAR")

    for posicion in range(4):
        if plista[posicion] == "REVISAR":
            if entrada[posicion] in codigosecreto:
                for revisa in range(4):
                    if entrada[posicion] == codigosecreto[revisa] and not leido[revisa]:
                        plista[posicion] = emoji["CASI"]
                        leido[revisa] = True  
                        break

    for posicion in range(4):
        if plista[posicion] is "REVISAR":
            plista[posicion] = emoji["NO"]

    pista = ("".join(plista))
    print("{}\n{}".format(numero, str(pista)))


def juego():
    global intentos

    if facil:
        intentos = 10
        codigosecreto = numerosnorepetidos()
    elif medio:
        intentos = 6
        repetir = random.randint(1, 2)
        if repetir == 1:
            codigosecreto = numerosrepetidos()
        else:
            codigosecreto = numerosnorepetidos()
    elif dificil:
        intentos = 4
        codigosecreto = numerosrepetidos()

    print("Todo listo! Ya he elegido un numero!")

    while True:
        
        entrada = input("\nEscribe un numero de cuatro digitos: ")

        if len(entrada) == 4:
            
            if entrada == codigosecreto:
                emojicod = " ".join([emoji[num] for num in codigosecreto])
                print("¡Has ganado y adivinado el codigo '{}'! Tenias {} intento(s)".format(emojicod, intentos))
                break
            if intentos > 1:
                    intentos -= 1
                    print("Tienes {} intentos restantes".format(intentos))
                    print("\nPistas:")
                    corregir(codigosecreto, entrada)

            else:
                emojicod = " ".join([emoji[num] for num in codigosecreto])
                print("¡Te han acabado los intentos y has perdido! El codigo secreto era '{}'".format(emojicod))
                break

        else:
            print("Por favor escribe un numero con cuatro digitos")

    siono = input("Quieres jugar otra vez? (S/n): ").lower()
    if siono != "s":
        exit()

### PROGRAMA ###

tutorial()

while True:
    opciones()

    print("")
    if facil:
        print("ACUERDATE: Tendras {} intentos y no habran numeros repetidos".format(intentos))
    elif medio:
        print("ACUERDATE: Tendras {} intentos y puede haber numeros repetidos".format(intentos))
    else:
        print("ACUERDATE: Tendras {} intentos y habran numeros repetidos".format(intentos))
    print("")
    juego()

    facil = False
    medio = False
    dificil = False