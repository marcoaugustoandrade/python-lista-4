numeros = [10, 3, 7, 5, 4, 13, 24, 9]
numeros_ordenados = sorted(numeros)

print("Imprimindo lista ordenada: ")
for i in numeros_ordenados:
    print(i)

print("Imprimindo lista não ordenada: ")
for i in range(len(numeros_ordenados) - 1, -1, -1):
    print(numeros_ordenados[i])
