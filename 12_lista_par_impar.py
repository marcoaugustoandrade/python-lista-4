lista = [1, 6, 8, 9, 10, 12, 18, 20, 34, 19, 34, 35, 38, 39, 37, 47, 49, 50, 52, 56]
listaPares = []
listaImpares = []

for i in lista:
    if (i % 2 == 0):
        listaPares.append(i)
    else:
        listaImpares.append(i)

print("Lista de pares: ")
for i in listaPares:
    print("%d " % i, end = "")

print("\nLista de ímpares: ")
for i in listaImpares:
    print("%d " % i, end="")
