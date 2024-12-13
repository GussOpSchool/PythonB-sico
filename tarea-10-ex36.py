import random
import time
puntos = 0
record = 0

def intro():
    print("""En una epoca donde los gigantes governaban Menorca, nosotros necesitemos comida.
    Siguiendo el rastro del olor de la comida, nos encontramos con una bifurcacion.
    Al final de cada camino, hay un talayot. En uno viven los gigantes buenos que nos convidaran
    y en el otro son unos canibales hambrientos que comeran sea lo que sea.
    """)

def cambiatalayot():
    talayot = ""
    while talayot != "1" and talayot != "2":
        talayot = input("A cual talayot quieres ir? Introduce 1 o 2: ")
    return talayot

def trobada(cambiatalayot):
    global puntos, record
    print ("Te acercas al talayot...")
    time.sleep(2)
    print ("Esta oscuro y es tenebroso...")
    time.sleep(2)
    print ("Un grande gigante salta en frente tuyo, te coge y...")
    print ("")
    time.sleep(2)
    giganteamigo = random.randint (1, 2)
    if cambiatalayot == str(giganteamigo):
        puntos += 1
        print ("Te convida a comer! Has ganado y tienes {} punto(s)!".format(puntos))
    else:
        if puntos >= record:
            record = puntos
        print ("Te comes de una vez! ÑAMÑAMÑAM Tu record es {} punto(s)".format(record))
        puntos = 0

# Funció principal 
nuevopartido = ("si")
while nuevopartido == ("s") or nuevopartido == ("si"):
    intro()
    ntalayot = cambiatalayot()
    trobada(ntalayot)
    nuevopartido = input("Quieres volver a comer (jugar)? Introduce si o no: ")
    print("\n")
