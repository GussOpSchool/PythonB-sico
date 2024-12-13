lista = list(range(1, 6))

for iteracion in range(5):
    reversolista = list(reversed(lista))
    reversolista = " ".join(map(str, reversolista))
    print(reversolista)
    lista.pop()
