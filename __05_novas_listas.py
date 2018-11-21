numeros = [0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 10, 11, 11, 12, 13, 15, 15]

intervalo_1_a_5 = []
intervalo_8_a_12 = []
pares = []
impares = []
multiplos_de_5_e_3 = []
lista_inversa = []

for i in numeros:
    if numeros[i] <= 5:
        intervalo_1_a_5.append(numeros[i])
    if 8 <= numeros[i] <= 12:
        intervalo_8_a_12.append(numeros[i])
    if numeros[i] % 3 == 0 and numeros[i] % 5 == 0:
        multiplos_de_5_e_3.append(numeros[i])
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])


for i in range((len(numeros) - 1), -1, -1):
    lista_inversa.append(numeros[i])

print("Intervalo de 1 a 5: ")
print(intervalo_1_a_5)
print("Intervalo de 8 a 12: ")
print(intervalo_8_a_12)
print("Números pares: ")
print(pares)
print("Números ímpares: ")
print(impares)
print("Múltiplos de 3 e 5: ")
print(multiplos_de_5_e_3)
print("Lista inversa: ")
print(lista_inversa)
