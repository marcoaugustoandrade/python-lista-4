numeros = [10, 5, 7, 10, -2, -4, 19]

maior = numeros[0]
soma = 0
primeiro = 0
media = 0
soma_negativo = 0

for i in range(0, len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
    soma += numeros[i]
    if numeros[i] == numeros[0]:
        primeiro += 1
    media += numeros[i]
    if numeros[i] < 0:
        soma_negativo += numeros[i]

print("O maior número é o %d." % maior)
print("A soma de todos elementos é %d." % soma)
print("O número de ocorrências do primeiro elemento é %d." % primeiro)
print("A média dos elementos da lista é %d." % (media / len(numeros)))
print("A soma dos elementos negativos da lista é %d" % soma_negativo)
