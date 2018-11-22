lista = [2.5, 7.5, 10.0, 4.0]
diferenca = []
media = sum(lista) / len(lista)

for i in lista:
    if media > i:
        diferenca.append(media - i)
    elif media < i:
        diferenca.append(i - media)
    else:
        diferenca.append(0)

print("O elemento mais próximo da média é %.2f." % lista[diferenca.index(min(diferenca))])
