ano = int(input("Deme un ano y te dire si es bisexto o no: "))

def esbisexto():
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("El ano {} es bisexto".format(ano))
    else:
        print("El ano {} NO es bisexto".format(ano))

esbisexto()