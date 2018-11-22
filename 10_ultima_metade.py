lista = [10, 2, 3, 9, 7, 99, 14, 4]

# print(lista[-int(len(lista) / 2):], lista[:int(len(lista) / 2)])

for i in lista[-int(len(lista) / 2):]:
    print(i, end =" ")

for i in lista[:int(len(lista) / 2)]:
    print(i, end =" ")
