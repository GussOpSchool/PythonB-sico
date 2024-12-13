palabra = input("Deme una palabra y te dare las vocales que tiene: ").lower()
A = E = I = O = U = 0

def contarvocales():
    global A, E, I, O, U

    for letra in palabra:
        match letra:
            case "a":
                A += 1
            case "e":
                E += 1
            case "i":
                I += 1
            case "o":
                O += 1
            case "u":
                U += 1
    
    print("Estas son las vocales encontradas en la palabra '{}':".format(palabra))
    print("A: {}\nE: {}\nI: {}\nO: {}\nU: {}".format(A, E, I, O, U))

contarvocales()