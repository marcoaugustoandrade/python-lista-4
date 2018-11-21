lista = [2.5, 7.5, 10.0, 4.0]
diferenca = []
[diferenca.append((sum(lista) / len(lista)) - i) if (sum(lista) / len(lista)) > i else diferenca.append(i - (sum(lista) / len(lista))) for i in lista]
print("O elemento mais próximo da média é %.2f." % lista[diferenca.index(min(diferenca))])
