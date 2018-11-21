from random import randint

lancamentos = []
quantidade = {}

for i in range(0,100):
    lancamentos.append(randint(0,100))

# for i in range(0,100):
#     for j in range(0,100):
#         if lancamentos[j] == i:
#             quantidade[i] += 1

print(quantidade)
