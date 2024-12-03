def espalindromo(cadena):
    if cadena[::-1] == cadena:
        print("La cadena '{}' es un palindromo:\n".format(cadena))
        print("Cadena original: {}".format(cadena))
        print("Cadena invertida: {}".format(cadena[::-1]))
    else:
        print("La cadena '{}' no es un palindromo:\n".format(cadena))
        print("Cadena original: '{}'".format(cadena))
        print("Cadena invertida: '{}'".format(cadena[::-1]))
    return cadena

espalindromo(input("Deme una frase que yo la invertire: "))