notas = []

for i in range(1,11):
    notas.append(input('Informe a nota do %dº aluno: ' % i))

total = 0
for i in notas:
    total += int(i)

print("A média de notas é %.2f." % (total / 10))
